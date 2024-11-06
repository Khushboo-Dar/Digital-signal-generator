#NRZ-I
import numpy as np
import matplotlib.pyplot as plt

# Function to perform NRZ-I encoding
def nrz_i_encode(data, voltage_level):
    encoded_signal = np.zeros(len(data))
    current_level = voltage_level

    for i in range(len(data)):
        if data[i] == 1:
            current_level = -current_level  # Invert level on '1'
        encoded_signal[i] = current_level

    return encoded_signal

# User input
data_bits = input("Enter the binary data sequence (e.g., '101011'): ")
voltage_level = float(input("Enter the peak voltage level in Volts (e.g., 5): "))

# Convert input data to an array of integers
data = np.array([int(bit) for bit in data_bits])

# Perform NRZ-I encoding
encoded_signal = nrz_i_encode(data, voltage_level)

# Plot the encoded signal
plt.figure(figsize=(10, 4))
plt.step(range(len(encoded_signal)), encoded_signal, where='mid')
plt.ylim(-1.5 * voltage_level, 1.5 * voltage_level)
plt.title("NRZ-I Encoded Signal")
plt.xlabel("Bit Index")
plt.ylabel("Voltage Level (V)")
plt.grid(True)
plt.show()
