import numpy as np
import matplotlib.pyplot as plt


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
            


def generate_time_points(signal_length, bitrate, is_manchester=False):
    """Generate time points for the signal."""
    if is_manchester:
        return np.linspace(0, signal_length/(2*bitrate), signal_length+1)
    else:
        return np.linspace(0, signal_length/bitrate, signal_length+1)

def prepare_plot_data(signal):
    """Prepare signal data for plotting by extending the last value."""
    return np.array(signal + [signal[-1]])

def plot_hdb3(signal, time_points, title, bitrate, bits):
    """Plot HDB3 signal with markers and labels."""
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

    signal = encode_hdb3(bits)
    print(signal)
    time_points = generate_time_points(len(signal), bitrate)
    plot_hdb3(signal, time_points, 'HDB3 Encoding', bitrate, bits)

if __name__ == '__main__':
    main()


    