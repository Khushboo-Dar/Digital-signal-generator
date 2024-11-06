import numpy as np
import matplotlib.pyplot as plt

def B8ZS(signal):
    n = len(signal)
    prev = -1  # Last non-zero voltage level
    count = 0  # Count of consecutive zeros

    for i in range(n):
        if signal[i] == 0:
            count += 1
        else:
            prev = signal[i]
            count = 0  # Reset count when a '1' is encountered

        # Apply B8ZS substitution when there are 8 consecutive zeros
        if count == 8:
            v = prev
            # Insert the B8ZS pattern
            signal[i] = v
            signal[i - 1] = -v
            signal[i - 3] = -v
            signal[i - 4] = v
            count = 0  # Reset count after substitution
    
    return signal

# Get input from the user
user_input = input("Enter a binary sequence (1s and 0s) without spaces (e.g., 110010000100000): ")

# Convert input string to a numpy array of integers (0s and 1s)
signal = np.array([int(bit) for bit in user_input])

# Apply B8ZS encoding
encoded_signal = B8ZS(signal.copy())

# Plot the original and encoded signals
plt.figure(figsize=(10, 6))

# Plot original signal
plt.subplot(2, 1, 1)
plt.step(np.arange(len(signal)), signal, where='post', label='Original Signal')
plt.title('Original Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)

# Plot encoded signal
plt.subplot(2, 1, 2)
plt.step(np.arange(len(encoded_signal)), encoded_signal, where='post', label='Encoded Signal', color='orange')
plt.title('B8ZS Encoded Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)

# Display the plot
plt.tight_layout()
plt.show()
