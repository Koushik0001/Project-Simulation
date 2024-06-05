import math
import numpy as np
import simu_NOMA
import simu_OMA
import csv

from inputs import uav
from inputs import environment_parameters, system_parameters
from rician_factor import get_rician_factor
import small_scale_fading as ssf

def generate_uniform_points_in_circle(n, r):
    # Generate n random angles uniformly distributed between 0 and 2*pi
    angles = np.random.uniform(0, 2 * np.pi, n)
    
    # Generate n random radii uniformly distributed between 0 and r, scaled by square root to ensure uniform distribution in the circle
    radii = np.sqrt(np.random.uniform(0, r**2, n))
    
    # Convert polar coordinates to Cartesian coordinates
    x = radii * np.cos(angles)
    y = radii * np.sin(angles)
    
    return list(zip(x, y))


def simulate(no_users, height=None):
    # user division in service classes
    no_service_classes = len(uav['service_classes'])
    users_in_sclass = [(no_users // no_service_classes) for _ in range(no_service_classes)]
    extra_users = no_users % no_service_classes

    i = 0
    while i<no_users and extra_users > 0:
        users_in_sclass[i] += 1
        extra_users -= 1
        i += 1

    # generating user data
    uniform_coordinates = generate_uniform_points_in_circle(no_users, system_parameters['cell_redius'])
    users = []

    i = 0
    for s in range(no_service_classes):
        for si in range(users_in_sclass[s]):
            user = dict()
            
            user['coordinate'] = uniform_coordinates[i]
            user['th_data_rate'] = uav['service_classes'][s] * 1e6
            
            # Calculating euclidean distance between UAV and user           
            d = math.sqrt(user['coordinate'][0] ** 2 + user['coordinate'][1] ** 2 + height ** 2)
            
            # Calculating elevation angle of the UAV w.r.t. the user
            elevation_angle = (180/math.pi) * math.asin(height/d)

            # Calculating LOS probability
            pr_los = 1 / (1 + environment_parameters['a'] * math.exp(-environment_parameters['b'] * (elevation_angle - environment_parameters['a'])))

            # Calculating large-scale average pathloss
            eta_linear = 10 ** (environment_parameters['eta'] / 10)
            g = pr_los * (d ** (-environment_parameters['alpha'])) + (1 - pr_los) * eta_linear * (d ** (-environment_parameters['alpha']))
            g_dB = 10 * math.log10(g)


            # Calculating Rician Factor
            K = get_rician_factor(user['coordinate'][0], user['coordinate'][1], height)
            
            # Calculating small scall fading channel coefficient
            h_mag_sq = ssf.generate_sample(K)
            h_mag_sq_db = 10 * math.log10(h_mag_sq)

            # Calculating channel gain
            user['H_db'] = g_dB + h_mag_sq_db
            
            # Adding the user to the list of users
            users.append(user)
            i += 1

    H_db = [users[i]['H_db'] for i in range(no_users)]
    th_data_rate = [users[i]['th_data_rate'] for i in range(no_users)]

    

    # Get total power using NOMA
    association_matrix, power_matrix = simu_NOMA.noma_power_opt(
        system_parameters['no_prb'], 
        system_parameters['B'], 
        environment_parameters['noise_dBm'], 
        H_db, 
        th_data_rate
    )
    total_power_noma = 0
    for i in range(0, no_users):
        for j in range(0, no_users):
            total_power_noma += association_matrix[i][j] * (
                (10 ** (power_matrix[i][j][0] / 10)) + (10 ** (power_matrix[i][j][1] / 10))
            )
    total_power_noma_dbm = 10 * math.log10(total_power_noma)
    if(total_power_noma_dbm > uav['max_power']):
        print(f"PowerConstraintError(NOMA): required power {total_power_noma_dbm} dBm > avilable power {uav['max_power']} dBm \nfor\n\t users={no_users}\n\t height={height} m\n")
    
    # Calculate power efficiency of NOMA
    pe_noma = 10 * math.log10(sum(th_data_rate) * 1e6/total_power_noma)



    # Get total power using OMA
    num_prb_per_user, power_user = simu_OMA.oma_power_opt(
        system_parameters['no_prb'], 
        system_parameters['B'], 
        environment_parameters['noise_dBm'], 
        H_db, 
        th_data_rate
    )
    total_power_oma = 0
    if num_prb_per_user != 0:
        for i in range(0, no_users):
            total_power_oma += (10 ** (power_user[i] / 10)) * num_prb_per_user
    total_power_oma_dbm = 10 * math.log10(total_power_oma)
    if(total_power_oma_dbm > uav['max_power']):
        print(f"PowerConstraintError(OMA): required power {total_power_oma_dbm} dBm > avilable power {uav['max_power']} dBm \nfor\n\t users={no_users}\n\t height={height} m\n")

    # Calculate power efficiency of OMA
    pe_oma = 10 * math.log10(sum(th_data_rate) * 1e6/total_power_oma)


    return (total_power_noma_dbm, total_power_oma_dbm, pe_noma, pe_oma, H_db)


if __name__== '__main__':
    
    # Comparison of average power and power efficiency of NOMA and OMA 
    no_of_users = list()
    total_powers_noma = list()
    total_powers_oma = list()
    pes_noma = list()
    pes_oma = list()

    for i in range(20, 101, 20):
        (total_power_noma, total_power_oma, pe_noma, pe_oma, _) = simulate(i, 40)
        no_of_users.append(i)
        total_powers_noma.append(total_power_noma)
        total_powers_oma.append(total_power_oma)
        pes_noma.append(pe_noma)
        pes_oma.append(pe_oma)



    # Name of the CSV file
    numberOfUsers_vs_power = 'data_numberOfUsers_vs_power.csv'

    # Write data to CSV
    with open(numberOfUsers_vs_power, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header
        writer.writerow(['number_of_users', 'NOMA_total_power', 'OMA_total_power', 'NOMA_power_efficiency', 'OMA_power_efficiency'])
        
        # Write the data rows
        for i in range(len(no_of_users)):
            writer.writerow([
                no_of_users[i],
                total_powers_noma[i],
                total_powers_oma[i],
                pes_noma[i],
                pes_oma[i]
            ])

    print(f"Data written to {numberOfUsers_vs_power} successfully!")

    # For plotting Height vs Power Efficiency
    heights = list()

    # Height vs Power with 40 users
    h_total_powers_noma_40 = list()
    h_total_powers_oma_40 = list()
    h_pes_noma_40 = list()
    h_pes_oma_40 = list()
    h_data_40 = list()

    for h in range(uav['min_height'], uav['max_height']+1, 10):
        (h_total_power_noma_40, h_total_power_oma_40, h_pe_noma_40, h_pe_oma_40, h_db_40) = simulate(40, h)
        heights.append(h)
        h_total_powers_noma_40.append(h_total_power_noma_40)
        h_total_powers_oma_40.append(h_total_power_oma_40)
        h_pes_noma_40.append(h_pe_noma_40)
        h_pes_oma_40.append(h_pe_oma_40)

        # For plotting Average value of Height vs Channel Gain
        h_db_40.insert(0, h)
        h_data_40.append(h_db_40)

    # Height vs Power with 60 users
    h_total_powers_noma_60 = list()
    h_total_powers_oma_60 = list()
    h_pes_noma_60 = list()
    h_pes_oma_60 = list()
    h_data_60 = list()

    for h in range(uav['min_height'], uav['max_height']+1, 10):
        (h_total_power_noma_60, h_total_power_oma_60, h_pe_noma_60, h_pe_oma_60, h_db_60) = simulate(60, h)
        h_total_powers_noma_60.append(h_total_power_noma_60)
        h_total_powers_oma_60.append(h_total_power_oma_60)
        h_pes_noma_60.append(h_pe_noma_60)
        h_pes_oma_60.append(h_pe_oma_60)

        # For plotting Average value of Height vs Channel Gain
        h_db_60.insert(0, h)
        h_data_60.append(h_db_60)
    


    # Name of the CSV file
    height_vs_powerEfficiency = 'data_height_vs_powerEfficiency.csv'

   # Write data to CSV
    with open(height_vs_powerEfficiency, mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write the header
        writer.writerow(['height', 
                         'NOMA_total_power_40', 
                         'NOMA_total_power_60', 
                         'OMA_total_power_40', 
                         'OMA_total_power_60', 
                         'NOMA_power_efficiency_40', 
                         'NOMA_power_efficiency_60', 
                         'OMA_power_efficiency_40',
                         'OMA_power_efficiency_60'])
        
        # Write the data rows
        for i in range(len(heights)):
            writer.writerow([
                heights[i],
                h_total_powers_noma_40[i],
                h_total_powers_noma_60[i],
                h_total_powers_oma_40[i],
                h_total_powers_oma_60[i],
                h_pes_noma_40[i],
                h_pes_noma_60[i],
                h_pes_oma_40[i],
                h_pes_oma_60[i]
            ])

    print(f"Data written to {height_vs_powerEfficiency} successfully!")


    # For plotting Height vs Channel gain
    height_vs_channelGain = 'data_height_vs_channelGain.csv'

    # Write the data to a CSV file
    with open(height_vs_channelGain, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(h_data_40)

    print(f"Data written to {height_vs_channelGain} successfully!")
        

