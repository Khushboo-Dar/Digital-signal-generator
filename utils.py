# General utility functions, including finding the longest palindrome and plotting the signal.
import matplotlib.pyplot as plt
import numpy as np


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



"Centre expanding algorithm"
def longestPalindrome(s):
    if not s:
        return ""

    start, max_len = 0, 1

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    for i in range(len(s)):
        # Check for odd-length palindromes
        left1, right1 = expand_around_center(i, i)
        if right1 - left1 + 1 > max_len:
            start, max_len = left1, right1 - left1 + 1

        # Check for even-length palindromes
        left2, right2 = expand_around_center(i, i + 1)
        if right2 - left2 + 1 > max_len:
            start, max_len = left2, right2 - left2 + 1

    return s[start:start + max_len]


