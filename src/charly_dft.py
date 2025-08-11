import numpy as np
import matplotlib.pyplot as plt
from src.utils.grapher import discrete_plotter, continuous_plotter


def dft(x_n):
    N = len(x_n)
    X = np.zeros(N, dtype=complex)
    for m in range(N):
        suma = 0.0 + 0.0j
        for n in range(N):
            suma+=x_n[n]*(np.cos(2*np.pi*n*m/N)-1j*np.sin(2*np.pi*n*m/N))
        X[m] = suma
    return X


def dft_analysis(dft, fs):

    dft = np.asarray(dft)
    N = dft.size
    freqs = [(m*fs)/N for m in range(N)]

    plot_data = [
        (np.abs(dft), "Magnitude", "Mag"),
        (dft.real, "Real Part", "Re"),
        (np.angle(dft), "Ángulo de fase", "Angle"),
        (dft.imag, "Imaginary Part", "Imag"),
    ]

    fig, axs = plt.subplots(2, 2, figsize=(10, 6))
    axs = axs.flatten() 
    for i, (y, title, ylabel) in enumerate(plot_data):
        axs[i].stem(freqs, y)
        axs[i].set_title(title)
        axs[i].set_ylabel(ylabel)
        axs[i].set_xlabel("Frequency")
        axs[i].grid(True)
    plt.tight_layout()
    plt.show()    
        

def x(t):
    x_t = np.sin(2*np.pi*1000*t) + 0.5*np.sin(2*np.pi*2000*t+3/4*np.pi)
    return x_t


def discretization(duration, fs):
    N = duration*fs
    n = np.arange(N)
    x_n = x(n/fs)
    discrete_plotter(n, x_n, "Discrete Signal", "Discrete", "Samples", "Amplitude")
    DFT = dft(x_n)
    dft_analysis(DFT, fs)