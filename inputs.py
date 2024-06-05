uav = {
    'coordinate': (0, 0),
    'height': 40,                      # in meters
    'service_classes': [1, 3, 5, 20],   # data rate in different service classes
    'min_height': 10,                   # minimum height of the UAV
    'max_height': 130,                  # maximum height of the UAV
    'service_classes': [1, 3, 5, 25],   # data rate in different service classes
    'max_power': 46                     # maximum transmit power of the UAV, in dBm    
}

environment_parameters={
    'k_0': 5,           # value of Rician factor at 0 radian elevation angle, in dB
    'k_90': 15,         # value of Rician factor at pi/2 radian elevation angle, in dB 
    'a': 11.95,         # parameter for urban environment
    'b': 0.136,         # parameter for urban environment
    'eta': 20,          # excessive attenuation factor for Non-LoS links, in dB
    'alpha': 3,         # path loss exponent
    'noise_dBm': -174   # noise density in dBm/Hz
}

system_parameters={
    'B': 720000,            # PRB bandwidth in Hz
    'no_prb': 135,          # Number of PRBs
    'cell_redius': 40       # in meters  
}