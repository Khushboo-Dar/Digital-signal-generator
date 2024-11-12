import matplotlib.pyplot as plt
import numpy as np
from utils import generate_time_points, prepare_plot_data, plot_differential_manchester, longestPalindrome

# for differential manchester encoding when bit is 0 we change the level of signal, 
# and when bit is 1 we keep the level same as previous
def encode_differential_manchester(stream):
    signal = []
    current_level = 1 #assume that previos level is 1
    
    for bit in stream:
        if bit == '0':
            current_level = -current_level
            signal.extend([current_level, -current_level])
        else:
            signal.extend([current_level, -current_level])
    
    return signal

def decode_differential_manchester(signal):
    decoded = []
    prev_level = 1
    for i in range(0, len(signal), 2):
        if signal[i] == prev_level:
            decoded.append('1')
        elif signal[i] == -prev_level:
            decoded.append('0')
        else:
            raise ValueError("Invalid signal")
        prev_level = signal[i]
    return ''.join(decoded)

def main_differential_manchester():
    bitrate = float(input("Enter bitrate (bits per second): "))
    bits = input("Enter data stream: ")
    manchester_signal = encode_differential_manchester(bits)
    manchester_time = generate_time_points(len(manchester_signal), bitrate, True)
    print("Differential Manchester Encoded Signal:", manchester_signal)
    print("Longset Palindrome in the signal:", longestPalindrome(bits))
    plot_differential_manchester(manchester_signal, manchester_time, f"Differential Manchester Encoding for bit stream: {bits}", bitrate, bits)
    decode = input("Do you want to decode the signal? (y/n): ")
    if decode.lower() == 'y' or decode.lower() == '':
        print("Decoded Signal:", decode_differential_manchester(manchester_signal))

