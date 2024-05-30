import numpy as np
from scipy.special import i0


# PDF function
def rician_pdf(omega, K_n, E_hn_squared=1):
    term1 = (K_n + 1) * np.exp(-K_n) / E_hn_squared
    term2 = np.exp(-(K_n + 1) * omega / E_hn_squared)
    term3 = i0(2 * np.sqrt(K_n * (K_n + 1) * omega / E_hn_squared))
    return term1 * term2 * term3

# Generate one likely sample using rejection sampling
def generate_sample(K_n, E_hn_squared=1):
    c = 1.5  # Scale factor for rejection sampling to ensure we cover the PDF adequately
    
    while True:
        # Generate a candidate sample from an exponential distribution
        candidate = np.random.exponential(scale=E_hn_squared / (K_n + 1))
        
        # Compute the acceptance probability
        u = np.random.uniform(0, c * rician_pdf(candidate, K_n, E_hn_squared))
        
        # Accept the candidate if it falls under the PDF curve
        if u <= rician_pdf(candidate, K_n, E_hn_squared):
            return linear_to_dbm(candidate)

# Convert the sample to dBm
def linear_to_dbm(value):
    return 10 * np.log10(value) + 30  # Adding 30 to convert from watts to milliwatts


if __name__=='__main__':
    # Generate one likely sample
    # Parameters
    K_n = 2  # Rician factor
    sample_dBm = generate_sample(K_n)
    print(f"The generated likely sample in dBm is: {sample_dBm:.5} dBm")
