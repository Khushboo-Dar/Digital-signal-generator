import matplotlib.pyplot as plt
import numpy as np
from utils import generate_time_points, prepare_plot_data, plot_nrz_l

def encode_nrz_l(stream):
    return [1 if bit == '1' else -1 for bit in stream]

def main_nrz_l():
    bitrate = float(input("Enter bitrate (bits per second): "))
    bits = input("Enter data stream: ")
    nrz_signal = encode_nrz_l(bits)
    nrz_time = generate_time_points(len(nrz_signal), bitrate)
    plot_nrz_l(nrz_signal, nrz_time, f"NRZ-L Encoding for bit stream: {bits}", bitrate, bits)

