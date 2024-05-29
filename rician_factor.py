import math
import numpy as np

from inputs import users
from inputs import uav

environment_parameters = {
    'k_0': 5,       # value of Rician factor at 0 radian elevation angle, in dB
    'k_90': 15,     # value of Rician factor at pi/2 radian elevation angle, in dB 
}

a = environment_parameters['k_0']
b = (2 / math.pi) * math.log(environment_parameters['k_90']/environment_parameters['k_0'])

def get_rician_factors():
    '''
        Return the Rician Factors of different UAV to user links based on the elevatioin angle of the UAV w.r.t. the user
    '''
    thetas = np.array([math.atan(uav['height']/math.sqrt(users[i]['coordinate'][0] ** 2 + users[i]['coordinate'][1] ** 2)) for i in range(0, len(users))])
    rician_factors = a * np.exp(b * thetas)

    return rician_factors


if __name__=='__main__':
    print(get_rician_factors())