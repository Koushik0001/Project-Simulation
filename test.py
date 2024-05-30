import numpy as np

def calculate_transmit_power(bandwidth_hz, channel_gain_db, noise_dbm, data_rate_mbps):
    # Convert data rate from Mbps to bps
    data_rate_bps = data_rate_mbps * 1e6
    
    # Calculate the required SNR (linear scale) using Shannon-Hartley theorem
    snr_linear = (2 ** (data_rate_bps / bandwidth_hz)) - 1
    
    # Convert SNR to dB
    snr_db = 10 * np.log10(snr_linear)
    
    # Calculate the noise power in dBm over the given bandwidth
    noise_power_dbm = noise_dbm + 10 * np.log10(bandwidth_hz)
    
    # Calculate the required transmit power in dBm
    transmit_power_dbm = noise_power_dbm + snr_db - channel_gain_db
    
    return transmit_power_dbm

# Example parameters
bandwidth_hz = 20e6  # 20 MHz
channel_gain_db = -80  # Channel gain in dB
noise_dbm = -100  # Noise power spectral density in dBm/Hz
data_rate_mbps = 10  # Data rate in Mbps

# Calculate transmit power
transmit_power_dbm = calculate_transmit_power(bandwidth_hz, channel_gain_db, noise_dbm, data_rate_mbps)

print(f"Required transmit power: {transmit_power_dbm:.2f} dBm")
