import numpy as np
import matplotlib.pyplot as plt
from utils import generate_time_points, prepare_plot_data, plot_hdb3, longestPalindrome

def encode_hdb3(bits):
    encoded = []
    current_level = 1
    last_substitution = 0
    consecutive_zeroes = 0

    for bit in bits:
        if bit == '1':
            encoded.append(current_level)
            current_level = -current_level
            last_substitution += 1
            consecutive_zeroes = 0
        else:
            consecutive_zeroes += 1
            if consecutive_zeroes == 4:
                for _ in range(3):
                    encoded.pop()
                if last_substitution % 2 == 0:
                    current_level = -current_level
                    encoded.extend([-current_level, 0, 0, -current_level])
                    last_substitution += 2
                else:
                    encoded.extend([0, 0, 0, -current_level])
                    last_substitution += 1
                consecutive_zeroes = 0
                last_substitution = 0
            else:
                encoded.append(0)
        
    return encoded
            

def main_hdb3():
    bitrate = float(input("Enter bitrate (bits per second): "))
    bits = input("Enter data stream: ")
    signal = encode_hdb3(bits)
    time_points = generate_time_points(len(signal), bitrate)
    print("HDB3 Encoded Signal:", signal)
    print("Longset Palindrome in the signal:", longestPalindrome(bits))
    plot_hdb3(signal, time_points, 'HDB3 Encoding', bitrate, bits)

    