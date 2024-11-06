#IN AMI encoding when the bit is 0 we send no signal, 
# and when bit is 1 we send signal with alternate polarity
import numpy as np
import matplotlib.pyplot as plt

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


def generate_time_points(signal_length, bitrate, is_manchester=False):
    """Generate time points for the signal."""
    if is_manchester:
        return np.linspace(0, signal_length/(2*bitrate), signal_length+1)
    else:
        return np.linspace(0, signal_length/bitrate, signal_length+1)

def prepare_plot_data(signal):
    """Prepare signal data for plotting by extending the last value."""
    return np.array(signal + [signal[-1]])


def plot_ami(signal, time_points, title, bitrate, bits):
    """Plot AMI signal with markers and labels."""
    fig, ax = plt.subplots(figsize=(12, 5))
    
    signal_plot = prepare_plot_data(signal)
    ax.plot(time_points, signal_plot, 'b-', label='Signal', drawstyle='steps-post')
    
    # Add bit boundaries
    for i in range(len(signal) + 1):
        ax.axvline(x=i/bitrate, color='r', linestyle='--', alpha=0.3)
    
    # Add bit labels
    for i in range(len(signal)):
        ax.text(i/bitrate + 0.5/bitrate, -1.5, bits[i],
                horizontalalignment='center')
    
    ax.grid(True)
    ax.set_xlabel(f'Time (seconds) [Bitrate: {bitrate} bps]')
    ax.set_ylabel('Amplitude')
    ax.set_title(title)
    ax.set_ylim(-2, 2)
    
    ax.axvline(x=-1, color='r', linestyle='--', alpha=0.3, label='Bit Boundaries')
    ax.legend()
    
    plt.tight_layout()
    plt.show()


def main():
    bitrate = int(input("Enter the bitrate: "))
    bits = input("Enter the data bits: ")
    signal = encode_ami(bits)
    time_points = generate_time_points(len(signal), bitrate)
    plot_ami(signal, time_points, 'AMI Encoding', bitrate, bits)

if __name__ == '__main__':
    main()