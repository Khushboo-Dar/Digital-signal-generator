#IN AMI encoding when the bit is 0 we send no signal, 
# and when bit is 1 we send signal with alternate polarity
import numpy as np
import matplotlib.pyplot as plt
from utils import generate_time_points, prepare_plot_data, plot_ami, longestPalindrome

def encode_ami(bits):
    """Encode data stream using AMI."""
    signal = []
    last_signal = -1
    for bit in bits:
        if bit == '1':
            last_signal *= -1 #invert the signal
            signal.append(last_signal)
        else:
            signal.append(0)
    return signal

def decode_ami(signal):
    """Decode AMI signal."""
    return ''.join(['1' if bit != 0 else '0' for bit in signal])

def main_ami():
    bitrate = float(input("Enter bitrate (bits per second): "))
    bits = input("Enter data stream: ")
    signal = encode_ami(bits)
    time_points = generate_time_points(len(signal), bitrate)
    print("AMI Encoded Signal:", signal)
    print("Longset Palindrome in the signal:", longestPalindrome(bits))
    print("Decoded Signal:", decode_ami(signal))
    plot_ami(signal, time_points, 'AMI Encoding', bitrate, bits)

