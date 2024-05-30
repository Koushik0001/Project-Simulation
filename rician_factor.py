import math
import numpy as np

from inputs import uav, environment_parameters

a = environment_parameters['k_0']
b = (2 / math.pi) * math.log(environment_parameters['k_90']/environment_parameters['k_0'])

def get_rician_factor(x, y):
    '''
        Return the Rician Factors of different UAV to user links based on the elevatioin angle of the UAV w.r.t. the user
    '''
    thetas = math.atan(uav['height']/math.sqrt(x ** 2 + y ** 2))
    rician_factor = a * math.exp(b * thetas)

    return rician_factor


if __name__=='__main__':
    print(get_rician_factor(12, 19))