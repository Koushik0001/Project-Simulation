# This  Python script is used to generate rician channel coefficients
import math
import numpy as np
from numpy.random import standard_normal
import simu_NOMA
import simu_OMA

from inputs import uav
from rician_factor import get_rician_factor
import small_scale_fading as ssf


environment_parameters={
    'g_dB': -34.89,     # channel gain at a distance of 1 meter in dB
    'alpha': 2,         # path loss exponent
    'noise_dBm': -174   # noise density in dBm/Hz
}

system_parameters={
    'b': 180000,            # PRB bandwidth in Hz
    'total_BW': 15000000,    # total bandwidth in Hz
    'cell_redius': 400        # in meters  
}
def generate_uniform_points_in_circle(n, r):
    # Generate n random angles uniformly distributed between 0 and 2*pi
    angles = np.random.uniform(0, 2 * np.pi, n)
    
    # Generate n random radii uniformly distributed between 0 and r, scaled by square root to ensure uniform distribution in the circle
    radii = np.sqrt(np.random.uniform(0, r**2, n))
    
    # Convert polar coordinates to Cartesian coordinates
    x = radii * np.cos(angles)
    y = radii * np.sin(angles)
    
    return list(zip(x, y))

# user division in service classes
no_users = int(input('Enter number of users: '))
no_service_classes = len(uav['service_classes'])
users_in_sclass = [(no_users // no_service_classes) for _ in range(no_service_classes)]
extra_users = no_users % no_service_classes

i = 0
while i<no_users and extra_users > 0:
    users_in_sclass[i] += 1
    extra_users -= 1
    i += 1

print(users_in_sclass)

# generating user data
uniform_coordinates = generate_uniform_points_in_circle(no_users, system_parameters['cell_redius'])
users = []

i = 0
for s in range(no_service_classes):
    for si in range(users_in_sclass[s]):
        user = dict()
        user['coordinate'] = uniform_coordinates[i]
        user['th_data_rate'] = uav['service_classes'][s] * 1e6
        K = get_rician_factor(user['coordinate'][0], user['coordinate'][1])
        h_mag_sq = ssf.generate_sample(K)
        d = math.sqrt(user['coordinate'][0] ** 2 + user['coordinate'][1] ** 2 + uav['height'] ** 2)
        H_linear = (10 ** (environment_parameters['g_dB'] / 10)) * (h_mag_sq) / (d**environment_parameters['alpha'])
        user['H_db'] = 10 * math.log10(H_linear)
        users.append(user)
        i += 1
print(users)

H_db = [users[i]['H_db'] for i in range(no_users)]
th_data_rate = [users[i]['th_data_rate'] for i in range(no_users)]


association_matrix, power_matrix = simu_NOMA.noma_power_opt(
    math.floor(system_parameters['total_BW'] / system_parameters['b']), 
    system_parameters['b'], 
    environment_parameters['noise_dBm'], 
    H_db, 
    th_data_rate
)

print(power_matrix)
num_prb_per_user, power_user = simu_OMA.oma_power_opt(
    math.floor(system_parameters['total_BW'] / system_parameters['b']), 
    system_parameters['b'], 
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

total_power_oma = 0
if num_prb_per_user != 0:
    for i in range(0, no_users):
        total_power_oma += (10 ** (power_user[i] / 10)) * num_prb_per_user

print(f"Total number of users = {no_users}")
print(f"Total power consumed using OMA = {total_power_oma} mW")
print(f"Total power consumed using NOMA = {total_power_noma} mW")
