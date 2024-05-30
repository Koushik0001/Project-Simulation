uav = {
    'coordinate': (0, 0),
    'height': 100,                      # in meters
    'service_classes': [1, 3, 5, 20]    # data rate in different service classes
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
    'B': 180000,            # PRB bandwidth in Hz
    'total_BW': 15000000,    # total bandwidth in Hz
    'cell_redius': 150        # in meters  
}