uav = {
    'coordinate': (0, 0),
    'height': 300,                      # in meters
    'service_classes': [1, 3, 5, 20]    # data rate in different service classes
}

environment_parameters={
    'k_0': 5,           # value of Rician factor at 0 radian elevation angle, in dB
    'k_90': 15,         # value of Rician factor at pi/2 radian elevation angle, in dB 
    'g_dB': -34.89,     # channel gain at a distance of 1 meter in dB
    'alpha': 2,         # path loss exponent
    'noise_dBm': -174   # noise density in dBm/Hz
}

system_parameters={
    'b': 180000,            # PRB bandwidth in Hz
    'total_BW': 15000000,    # total bandwidth in Hz
    'cell_redius': 400        # in meters  
}