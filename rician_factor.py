import math
import numpy as np

from inputs import uav, environment_parameters

k_0_linear = 10 ** (environment_parameters['k_0'] / 10)
k_90_linear = 10 ** (environment_parameters['k_90'] / 10)

a = k_0_linear
b = (2 / math.pi) * math.log(k_90_linear/k_0_linear)

def get_rician_factor(x, y, height):
    '''
        Return the Rician Factors of different UAV to user links based on the elevatioin angle of the UAV w.r.t. the user
    '''

    theta = math.atan(height/math.sqrt(x ** 2 + y ** 2))
    rician_factor = a * math.exp(b * theta)

    return rician_factor


if __name__=='__main__':
    print(get_rician_factor(12, 19))