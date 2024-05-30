# This  Python script is used to generate rician channel coefficients
import math
import numpy as np
from numpy.random import standard_normal
import simu_NOMA
import simu_OMA

from inputs import uav


environment_parameters={
    'g_dB': -34.89,     # channel gain at a distance of 1 meter in dB
    'alpha': 2,         # path loss exponent
    'noise_dBm': -174   # noise density in dBm/Hz
}

system_parameters={
    'b': 180000,            # PRB bandwidth in Hz
    'total_BW': 15000000    # total bandwidth in Hz
}
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

# # Large scale channel attenuation

# lower_bound = -10  # in meter
# upper_bound = 10  # in meter

# random_users_x = np.random.uniform(lower_bound, upper_bound, n)
# random_users_y = np.random.uniform(lower_bound, upper_bound, n)

# d = np.sqrt(random_users_x**2 + random_users_y**2 + height**2)

# H_dB = g_dB * (h_mag_dB**2) / (d**alpha)


# R = np.random.randint(5, 100 + 1, n)  # list of threshold data rates of the users


# association_matrix, power_matrix = simu_NOMA.noma_power_opt(
#     math.floor(total_BW / b), b, noise_dBm, H_dB.tolist(), R.tolist()
# )
# num_prb_per_user, power_user = simu_OMA.oma_power_opt(
#     math.floor(total_BW / b), b, noise_dBm, H_dB.tolist(), R.tolist()
# )


# total_power_noma = 0
# for i in range(0, n):
#     for j in range(0, n):
#         total_power_noma += association_matrix[i][j] * (
#             (10 ** (power_matrix[i][j][0] / 10)) + (10 ** (power_matrix[i][j][1] / 10))
#         )

# total_power_oma = 0
# if num_prb_per_user != 0:
#     for i in range(0, n):
#         total_power_oma += (10 ** (power_user[i] / 10)) * num_prb_per_user

# print(f"Total number of users = {n}")
# print(f"Total power consumed using OMA = {total_power_oma} mW")
# print(f"Total power consumed using NOMA = {total_power_noma} mW")
