import numpy as np
import matplotlib.pyplot as plt

def pcm(A, fm, fs, n):
    # Generate the continuous cosine signal
    t = np.arange(0, 1, 1 / (100 * fm))
    x = A * np.cos(2 * np.pi * fm * t)

    # Sampling
    ts = np.arange(0, 1, 1 / fs)
    xs = A * np.cos(2 * np.pi * fm * ts)

    # Quantization
    L = 2**n - 1  # Number of quantization levels
    x1 = (xs + A) / (2 * A) * L  # Normalize and scale to quantization levels
    xq = np.round(x1)  # Quantized signal levels
    r = (xq / L) * 2 * A - A  # Reconstruction from quantized levels

    # Encoding
    y = []
    for value in xq:
        binary = format(int(value), f'0{n}b')  # Convert each level to binary
        y.extend([int(bit) for bit in binary])  # Flatten to binary bit sequence

    # Calculate parameters
    MSE = np.mean((xs - r)**2)
    Bitrate = n * fs
    Stepsize = 2 * A / L
    QNoise = (Stepsize**2) / 12

    # Plotting
    plt.figure(1)
    plt.plot(t, x, label='Original Signal', linewidth=2)
    plt.title('Sampling')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.stem(ts, xs, 'r', markerfmt='ro', linefmt='r-', basefmt=" ", label='Sampled Signal')
    plt.legend()
    plt.grid(True)

    plt.figure(2)
    plt.stem(ts, x1, 'g', markerfmt='go', linefmt='g-', basefmt=" ", label='Sampled Signal (Quantized)')
    plt.stem(ts, xq, 'r', markerfmt='ro', linefmt='r-', basefmt=" ", label='Quantized Signal')
    plt.plot(ts, xq, '--r')
    plt.title('Quantization')
    plt.xlabel('Time (s)')
    plt.ylabel('Quantization Levels')
    plt.legend()
    plt.grid(True)

    plt.figure(3)
    plt.step(range(len(y)), y, 'b', where='post', linewidth=2)
    plt.title('Encoding')
    plt.xlabel('Bits')
    plt.ylabel('Binary Signal')
    plt.grid(True)

    plt.show()

    return y, Bitrate, MSE, Stepsize, QNoise

def main_pcm():
    # Get user input
    A = float(input("Enter the amplitude of the cosine signal (A): "))
    fm = float(input("Enter the frequency of the cosine signal (fm): "))
    fs = float(input("Enter the sampling frequency (fs): "))
    n = int(input("Enter the number of bits per sample (n): "))

    # Run the PCM function
    y, Bitrate, MSE, Stepsize, QNoise = pcm(A, fm, fs, n)

    # Display results
    print(f"Bitrate: {Bitrate} bits per second")
    print(f"Mean Square Error (MSE): {MSE}")
    print(f"Step Size: {Stepsize}")
    print(f"Quantization Noise (QNoise): {QNoise}")
