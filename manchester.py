#manchester encoding

import numpy as np
import matplotlib.pyplot as plt

def main_manchester():
    """
    Line code MANCHESTER with user input
    """
    # Ask for binary input from the user
    binary_input = input("Enter the binary sequence (e.g., 10011010): ")
    
    # Convert the string input to a list of integers
    h = [int(bit) for bit in binary_input]
    
    # Set up the plot
    plt.figure()
    plt.title("Line code MANCHESTER")
    plt.grid(True)
    plt.ylim([-1.5, 1.5])
    plt.xlim([0, len(h)])
    
    # Time step for smooth plotting
    time_step = 0.01
    t_total = np.arange(0, len(h), time_step)
    signal = []

    # Generate Manchester encoding waveform
    for i, bit in enumerate(h):
        t_half = np.arange(i, i + 0.5, time_step)
        t_full = np.arange(i + 0.5, i + 1, time_step)

        if bit == 0:
            # For 0: high to low transition
            signal.extend([1] * len(t_half))
            signal.extend([-1] * len(t_full))
        else:
            # For 1: low to high transition
            signal.extend([-1] * len(t_half))
            signal.extend([1] * len(t_full))

    # Plotting the Manchester waveform
    plt.plot(t_total, signal, linewidth=2.5)
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.show()

