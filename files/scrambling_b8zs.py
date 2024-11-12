import numpy as np
import matplotlib.pyplot as plt

def B8ZS(signal):
    n=len(signal)
    prev=-1
    count=0
    for i in range(n):
        if signal[i]==0:
            count+=1
        else:
            prev=signal[i]
            count=0
        if count==8:
            v=prev
            signal[i]=v
            signal[i-1]=-v
            signal[i-3]=-v
            signal[i-4]=v
            count=0
    return signal

def lengthNstring(length, n):
    samplestring='01'
    result=''.join(np.random.choice(list(samplestring)) for _ in range(length))
    while '0'*n not in result:
        result=''.join(np.random.choice(list(samplestring)) for _ in range(length))
    return result

def main_b8zs():
    input_type=input("Enter '1' for a custom binary sequence or '2' to generate a random binary sequence: ")
    if input_type=='1':
        user_input=input("Enter a binary sequence (1s and 0s) without spaces (e.g., 110010000100000): ")
        signal=np.array([int(bit) for bit in user_input])
    elif input_type=='2':
        size=int(input("Enter the length of string: "))
        n_zeroes=int(input("Enter the required length of zeroes: "))
        signal_str=lengthNstring(size, n_zeroes)
        print("Generated signal with zero sequence:", signal_str)
        signal=np.array([int(bit) for bit in signal_str])
    else:
        print("Invalid option selected.")
        exit()

    encoded_signal=B8ZS(signal.copy())

    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)
    plt.step(np.arange(len(signal)), signal, where='post', label='Original Signal')
    plt.title('Original Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.grid(True)

    plt.subplot(2, 1, 2)
    plt.step(np.arange(len(encoded_signal)), encoded_signal, where='post', label='Encoded Signal', color='orange')
    plt.title('B8ZS Encoded Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.grid(True)

    plt.tight_layout()
    plt.show()
