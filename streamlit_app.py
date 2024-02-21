import streamlit_app as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

# Function to plot chi-square distribution
def plot_chi_square_distribution(degrees_of_freedom, alpha=0.05):
    # Generate x values for the positive side of the distribution
    x = np.linspace(0, 20, 1000)
    
    # Calculate the chi-square probability density function (PDF) for given degrees of freedom
    y = chi2.pdf(x, degrees_of_freedom)
    
    # Plot the absolute value of chi-square distribution
    plt.figure(figsize=(10, 6))
    plt.plot(x, np.abs(y), label=f'Degrees of Freedom: {degrees_of_freedom}')
    plt.title('One-Sided Chi-Square Distribution')
    plt.xlabel('x')
    plt.ylabel('Probability Density')
    plt.xlim(0, max(x))  # Limit x-axis to positive values
    plt.legend()
    plt.grid(True)
    
    # Add annotations for accept and reject values
    accept_value = chi2.ppf(1 - alpha, degrees_of_freedom)
    reject_value = chi2.ppf(alpha, degrees_of_freedom)
    plt.axvline(accept_value, color='green', linestyle='--', label='Accept Value')
    plt.text(accept_value, 0.01, f'Accept: {round(accept_value, 2)}', color='green', rotation=90, verticalalignment='bottom')
    plt.axvline(reject_value, color='red', linestyle='--', label='Reject Value')
    plt.text(reject_value, 0.01, f'Reject: {round(reject_value, 2)}', color='red', rotation=90, verticalalignment='bottom')
    
    plt.legend()
    st.pyplot(plt)

# Streamlit app
def main():
    st.title('One-Sided Chi-Square Distribution Visualization')
    degrees_of_freedom = st.number_input('Enter Degrees of Freedom:', min_value=1, value=5)
    alpha = st.slider('Select Significance Level (alpha):', min_value=0.01, max_value=0.10, step=0.01, value=0.05)
    plot_chi_square_distribution(degrees_of_freedom, alpha)

if __name__ == "__main__":
    main()
