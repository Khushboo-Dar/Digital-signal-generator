#manchester
import numpy as np
import matplotlib.pyplot as plt
from utils import longestPalindrome

def encode_manchester(binary_input):
    signal = []
    time_step = 0.01
    for bit in binary_input:
        if bit == '0':
            signal.extend([1] * 50 + [-1] * 50)
        else:
            signal.extend([-1] * 50 + [1] * 50)
    return signal

def decode_manchester(signal):
    decoded = []
    for i in range(0, len(signal), 100):
        if signal[i] == 1 and signal[i + 50] == -1:
            decoded.append('0')
        elif signal[i] == -1 and signal[i + 50] == 1:
            decoded.append('1')
        else:
            raise ValueError("Invalid Manchester encoded signal")
    return ''.join(decoded)

def main_manchester():
    binary_input = input("Enter the binary sequence (e.g., 10011010): ")
    manchester_signal = encode_manchester(binary_input)
    time_step = 0.01
    t_total = np.arange(0, len(manchester_signal) * time_step, time_step)

    print("Manchester Encoded Signal:", manchester_signal)
    print("Longest Palindrome in the signal:", longestPalindrome(binary_input))

    plt.figure()
    plt.plot(t_total, manchester_signal, linewidth=2.5)
    plt.title("Manchester Encoding")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.ylim([-1.5, 1.5])
    plt.show()

    decode = input("Do you want to decode the signal? (y/n): ")
    if decode.lower() == 'y' or decode.lower() == '':
        decoded_signal = decode_manchester(manchester_signal)
        print("Decoded Signal:", decoded_signal)
