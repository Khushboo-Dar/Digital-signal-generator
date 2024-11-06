import matplotlib.pyplot as plt
import numpy as np

def encode_nrz_l(stream):
    return [1 if bit == '1' else -1 for bit in stream]


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

def generate_time_points(signal_length, bitrate, is_manchester=False):
    """Generate time points for the signal."""
    if is_manchester:
        return np.linspace(0, signal_length/(2*bitrate), signal_length+1)
    else:
        return np.linspace(0, signal_length/bitrate, signal_length+1)

def prepare_plot_data(signal):
    """Prepare signal data for plotting by extending the last value."""
    return np.array(signal + [signal[-1]])

def plot_nrz_l(signal, time_points, title, bitrate, bits):
    """Plot NRZ-L signal with markers and labels."""
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

def plot_differential_manchester(signal, time_points, title, bitrate, bits):
    """Plot Differential Manchester signal with markers and labels."""
    fig, ax = plt.subplots(figsize=(12, 5))
    
    signal_plot = prepare_plot_data(signal)
    ax.plot(time_points, signal_plot, 'b-', label='Signal', drawstyle='steps-post')
    
    # Add bit boundaries and mid-bit markers
    for i in range(len(signal)//2 + 1):
        ax.axvline(x=i/bitrate, color='r', linestyle='--', alpha=0.3)
        if i < len(signal)//2:
            ax.axvline(x=(i+0.5)/bitrate, color='g', linestyle=':', alpha=0.3)
    
    # Add bit labels
    for i in range(len(signal)//2):
        ax.text(i/bitrate + 0.5/bitrate, -1.5, bits[i],
                horizontalalignment='center')
    
    ax.grid(True)
    ax.set_xlabel(f'Time (seconds) [Bitrate: {bitrate} bps]')
    ax.set_ylabel('Amplitude')
    ax.set_title(title)
    ax.set_ylim(-2, 2)
    
    ax.axvline(x=-1, color='r', linestyle='--', alpha=0.3, label='Bit Boundaries')
    ax.axvline(x=-1, color='g', linestyle=':', alpha=0.3, label='Mid-Bit')
    ax.legend()
    
    plt.tight_layout()
    plt.show()

def main():
    bitrate = float(input("Enter bitrate (bits per second): "))
    bits = input("Enter data stream: ")
    
    print("\nNRZ-L Encoding")
    nrz_signal = encode_nrz_l(bits)
    nrz_time = generate_time_points(len(nrz_signal), bitrate)
    print(f"Encoded signal: {nrz_signal}")
    plot_nrz_l(nrz_signal, nrz_time, 
               f"NRZ-L Encoding for bit stream: {bits}", 
               bitrate, bits)
    
    print("\nDifferential Manchester Encoding")
    manchester_signal = encode_differential_manchester(bits)
    manchester_time = generate_time_points(len(manchester_signal), bitrate, True)
    print(f"Encoded signal: {manchester_signal}")
    plot_differential_manchester(manchester_signal, manchester_time,
                               f"Differential Manchester Encoding for bit stream: {bits}",
                               bitrate, bits)

if __name__ == "__main__":
    main()