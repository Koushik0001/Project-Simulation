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
            
            if(height == None):
                d = math.sqrt(user['coordinate'][0] ** 2 + user['coordinate'][1] ** 2 + uav['height'] ** 2)
                elevation_angle = (180/math.pi) * math.asin(uav['height']/d)
            else:
                d = math.sqrt(user['coordinate'][0] ** 2 + user['coordinate'][1] ** 2 + height ** 2)
                elevation_angle = (180/math.pi) * math.asin(height/d)

            pr_los = 1 / (1 + environment_parameters['a'] * math.exp(-environment_parameters['b'] * (elevation_angle - environment_parameters['a'])))
            g_dB = 10 * math.log10(pr_los * (d ** (-environment_parameters['alpha'])) + (1 - pr_los) * environment_parameters['eta'] * (d ** (-environment_parameters['alpha'])))
            
            K = get_rician_factor(user['coordinate'][0], user['coordinate'][1])
            h_mag_sq_db = 10 * math.log10(ssf.generate_sample(K))
            
            
            user['H_db'] = g_dB + h_mag_sq_db
            
            users.append(user)
            i += 1


    H_db = [users[i]['H_db'] for i in range(no_users)]
    th_data_rate = [users[i]['th_data_rate'] for i in range(no_users)]


    association_matrix, power_matrix = simu_NOMA.noma_power_opt(
        math.floor(system_parameters['total_BW'] / system_parameters['B']), 
        system_parameters['B'], 
        environment_parameters['noise_dBm'], 
        H_db, 
        th_data_rate
    )


    num_prb_per_user, power_user = simu_OMA.oma_power_opt(
        math.floor(system_parameters['total_BW'] / system_parameters['B']), 
        system_parameters['B'], 
        environment_parameters['noise_dBm'], 
        H_db, 
        th_data_rate
    )


    total_power_noma = 0
    total_power_oma = 0
    
    for i in range(0, no_users):
        for j in range(0, no_users):
            total_power_noma += association_matrix[i][j] * (
                (10 ** (power_matrix[i][j][0] / 10)) + (10 ** (power_matrix[i][j][1] / 10))
            )

    if num_prb_per_user != 0:
        for i in range(0, no_users):
            total_power_oma += (10 ** (power_user[i] / 10)) * num_prb_per_user

    avg_power_noma = total_power_noma/no_users
    avg_power_oma = total_power_oma/no_users
    
    ee_noma = math.log(sum(th_data_rate) * 1e6/total_power_noma)
    ee_oma = math.log(sum(th_data_rate) * 1e6/total_power_oma)

    return (avg_power_noma, avg_power_oma, ee_noma, ee_oma)


if __name__== '__main__':
    
    # Comparison of average power and power efficiency of NOMA and OMA 
    no_of_users = list()
    avg_powers_noma = list()
    avg_powers_oma = list()
    ees_noma = list()
    ees_oma = list()

    for i in range(4, 81, 4):
        (avg_power_noma, avg_power_oma, ee_noma, ee_oma) = simulate(i)
        no_of_users.append(i)
        avg_powers_noma.append(10 * math.log10(avg_power_noma))
        avg_powers_oma.append(10 * math.log10(avg_power_oma))
        ees_noma.append(ee_noma)
        ees_oma.append(ee_oma)


    # Name of the CSV file
    csv_file_name = 'power_efficiency_comparison.csv'

    # Write data to CSV
    with open(csv_file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header
        writer.writerow(['number_of_users', 'NOMA_avg_power', 'OMA_avg_power', 'NOMA_power_efficiency', 'OMA_power_efficiency'])
        
        # Write the data rows
        for i in range(len(no_of_users)):
            writer.writerow([
                no_of_users[i],
                avg_powers_noma[i],
                avg_powers_oma[i],
                ees_noma[i],
                ees_oma[i]
            ])

    print(f"Data written to {csv_file_name}")

    # For plotting Height vs Power Efficiency
    heights = list()
    h_avg_powers_noma = list()
    h_avg_powers_oma = list()
    h_ees_noma = list()
    h_ees_oma = list()

    for h in range(uav['min_height'], uav['max_height']+1, 1):
        (h_avg_power_noma, h_avg_power_oma, h_ee_noma, h_ee_oma) = simulate(20, h)
        heights.append(h)
        h_avg_powers_noma.append(10 * math.log10(avg_power_noma))
        h_avg_powers_oma.append(10 * math.log10(avg_power_oma))
        h_ees_noma.append(ee_noma)
        h_ees_oma.append(ee_oma)


    # Name of the CSV file
    h_csv_file_name = 'power_efficiency_vs_height.csv'

    # Write data to CSV
    with open(h_csv_file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header
        writer.writerow(['height', 'NOMA_avg_power', 'OMA_avg_power', 'NOMA_power_efficiency', 'OMA_power_efficiency'])
        
        # Write the data rows
        for i in range(len(heights)):
            writer.writerow([
                heights[i],
                h_avg_powers_noma[i],
                h_avg_powers_oma[i],
                h_ees_noma[i],
                h_ees_oma[i]
            ])

    print(f"Data written to {h_csv_file_name}")