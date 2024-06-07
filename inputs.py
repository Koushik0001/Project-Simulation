uav = {
    'coordinate': (0, 0),
    'service_classes': [1, 3, 5, 20],   # data rate in different service classes
    'min_height': 10,                   # minimum height of the UAV
    'max_height': 130,                  # maximum height of the UAV
    'service_classes': [1, 3, 5, 25],   # data rate in different service classes
    'max_power': 46                     # maximum transmit power of the UAV, in dBm    
}

environment_parameters={
    'k_0': 5,           # value of Rician factor at 0 radian elevation angle, in dB
    'k_90': 15,         # value of Rician factor at pi/2 radian elevation angle, in dB 
    'k': 0.36,             # parameter for urban environment
    'omega': 0.21,         # parameter for urban environment
    'mu_los':1.6,             # in dB
    'mu_nlos': 23,           # in dB
    's': -40,                   # in dB
    'noise_dBm': -174   # noise density in dBm/Hz
}

system_parameters={
    'B': 720000,            # PRB bandwidth in Hz
    'no_prb': 135,          # Number of PRBs  
}