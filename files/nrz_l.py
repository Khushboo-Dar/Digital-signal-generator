import matplotlib.pyplot as plt
import numpy as np
from utils import generate_time_points, prepare_plot_data, plot_nrz_l, longestPalindrome

def encode_nrz_l(stream):
    return [1 if bit == '1' else -1 for bit in stream]

def decode_nrz_l(signal):
    return ''.join(['1' if bit > 0 else '0' for bit in signal])

def main_nrz_l():
    bitrate = float(input("Enter bitrate (bits per second): "))
    bits = input("Enter data stream: ")
    nrz_signal = encode_nrz_l(bits)
    nrz_time = generate_time_points(len(nrz_signal), bitrate)
    print("NRZ-L Encoded Signal:", nrz_signal)
    print("Longset Palindrome in the signal:", longestPalindrome(bits))
    plot_nrz_l(nrz_signal, nrz_time, f"NRZ-L Encoding for bit stream: {bits}", bitrate, bits)
    decode = input("Do you want to decode the signal? (y/n): ")
    if decode.lower() == 'y':
        print("Decoded Signal:", decode_nrz_l(nrz_signal))

