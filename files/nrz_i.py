import numpy as np
import matplotlib.pyplot as plt
from utils import longestPalindrome

#NRZ-I encoding
def nrz_i_encode(data, voltage_level):
    encoded_signal = np.zeros(len(data))
    current_level = voltage_level

    for i in range(len(data)):
        if data[i] == 1:
            current_level = -current_level
        encoded_signal[i] = current_level

    return encoded_signal

#NRZ-I decoding
def decode_nrz_i(signal, voltage_level):
    decoded_data = []
    current_level = voltage_level

    for level in signal:
        if level == current_level:
            decoded_data.append(0)
        else:
            decoded_data.append(1)
            current_level = level

    return ''.join(map(str, decoded_data))

def main_nrz_i():
    data_bits = input("Enter the binary data sequence (e.g., '101011'): ")
    voltage_level = float(input("Enter the peak voltage level in Volts (e.g., 5): "))
    data = np.array([int(bit) for bit in data_bits])
    encoded_signal = nrz_i_encode(data, voltage_level)
    print("NRZ-I Encoded Signal:", encoded_signal)
    print("Longest Palindrome in the signal:", longestPalindrome(data_bits))
    plt.figure(figsize=(10, 4))
    plt.step(range(len(encoded_signal)), encoded_signal, where='mid')
    plt.ylim(-1.5 * voltage_level, 1.5 * voltage_level)
    plt.title("NRZ-I Encoded Signal")
    plt.xlabel("Bit Index")
    plt.ylabel("Voltage Level (V)")
    plt.grid(True)
    plt.show()
    decode = input("Do you want to decode the signal? (y/n): ")
    if decode.lower() == 'y':
        print("Decoded Signal:", decode_nrz_i(encoded_signal, voltage_level))
