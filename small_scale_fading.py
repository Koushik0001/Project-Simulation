import numpy as np
from scipy.special import i0
import matplotlib.pyplot as plt


def rician_pdf(omega, K_n, E_hn_squared):
    term1 = (K_n + 1) * np.exp(-K_n) / E_hn_squared
    term2 = np.exp(-(K_n + 1) * omega / E_hn_squared)
    term3 = i0(2 * np.sqrt(K_n * (K_n + 1) * omega / E_hn_squared))
    return term1 * term2 * term3

def generate_rician_samples(K_n, E_hn_squared, num_samples):
    samples = []
    c = 1.5  # Scale factor for rejection sampling to ensure we cover the PDF adequately
    
    while len(samples) < num_samples:
        # Generate a candidate sample from an exponential distribution
        candidate = np.random.exponential(scale=E_hn_squared / (K_n + 1))
        
        # Compute the acceptance probability
        u = np.random.uniform(0, c * rician_pdf(candidate, K_n, E_hn_squared))
        
        # Accept or reject the candidate
        if u <= rician_pdf(candidate, K_n, E_hn_squared):
            samples.append(candidate)
    
    return np.array(samples)



if __name__=="__main__":
    
    # Generate samples

    # Parameters
    K_n = 3             # Rician factor
    E_hn_squared = 2    # Expected value of |h_n|^2
    num_samples = 10000
    samples = generate_rician_samples(K_n, E_hn_squared, num_samples)

    samples_db = 10 * np.log10(samples)

    # Plotting the histogram in dB
    plt.hist(samples_db, bins=50, density=True, alpha=0.6, color='g')

    # Plot the theoretical PDF in linear scale for comparison
    omega_values = np.linspace(0, max(samples), 1000)
    pdf_values = rician_pdf(omega_values, K_n, E_hn_squared)

    # Convert the omega values to dB
    omega_values_db = 10 * np.log10(omega_values + 1e-10)  # Adding a small value to avoid log(0)

    # Plot the theoretical PDF in dB
    plt.plot(omega_values_db, pdf_values, 'r', lw=2)

    plt.xlabel('$|h_n|^2$ (dB)')
    plt.ylabel('Density')
    plt.title('Histogram of Generated Samples in dB and Theoretical PDF')
    plt.show()

