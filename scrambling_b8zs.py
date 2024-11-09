import numpy as np
import matplotlib.pyplot as plt

def B8ZS(signal):
    n = len(signal)
    prev = -1  # Last non-zero voltage level
    count = 0  # Count of consecutive zeros

    # Iterate through the signal
    for i in range(n):
        if signal[i] == 0:
            count += 1  # Increase count of consecutive zeros
        else:
            prev = signal[i]  # Update the last non-zero voltage level
            count = 0  # Reset zero count when a '1' is encountered

        # Apply B8ZS substitution when there are 8 consecutive zeros
        if count == 8:
            v = prev
            # Apply the B8ZS pattern directly in-place
            signal[i] = v
            signal[i - 1] = -v
            signal[i - 3] = -v
            signal[i - 4] = v
            count = 0  # Reset count after substitution
    
    return signal

# Function to generate a random binary string with at least 'n' consecutive zeros
def lengthNstring(length, n):
    samplestring = '01'
    result = ''.join(np.random.choice(list(samplestring)) for _ in range(length))
    while '0' * n not in result:  # Ensure the string contains at least 'n' consecutive zeros
        result = ''.join(np.random.choice(list(samplestring)) for _ in range(length))
    return result

# Ask the user for input type
input_type = input("Enter '1' for a custom binary sequence or '2' to generate a random binary sequence: ")

if input_type == '1':
    # Get a custom binary sequence input from the user
    user_input = input("Enter a binary sequence (1s and 0s) without spaces (e.g., 110010000100000): ")
    # Convert input string to a numpy array of integers (0s and 1s)
    signal = np.array([int(bit) for bit in user_input])

elif input_type == '2':
    # Get the length of the binary sequence and required number of consecutive zeros
    size = int(input("Enter the length of string: "))
    n_zeroes = int(input("Enter the required length of zeroes: "))

    # Generate the binary signal with n consecutive zeros
    signal_str = lengthNstring(size, n_zeroes)
    print("Generated signal with zero sequence:", signal_str)

    # Convert the generated signal to a numpy array of integers (0s and 1s)
    signal = np.array([int(bit) for bit in signal_str])

else:
    print("Invalid option selected.")
    exit()

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
