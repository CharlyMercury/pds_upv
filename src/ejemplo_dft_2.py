import numpy as np
from src.utils.grapher import continuous_plotter, discrete_plotter


def dft_2():
    
    end_time = 0.1 # Segundos
    
    # Tiempo continuo
    t = np.linspace(0, end_time, 10000)
    x_t = 1.1*np.cos(2*np.pi*300*t) + \
        0.9*np.sin(2*np.pi*450*t+6*np.pi)+0.7*np.cos(2*np.pi*1200*t-4*np.pi) + \
        0.5*np.sin(2*np.pi*2600*t)+0.4*np.cos(2*np.pi*3300*t)
    continuous_plotter(t, x_t, "Señal Continua", "Continua", "Tiempo", "Amplitud")

    # Tiempo discreto
    fs = 8000
    n = np.arange(end_time*fs)
    x_n = 1.1*np.cos(2*np.pi*(300/fs)*n) + \
        0.9*np.sin(2*np.pi*(450/fs)*n+6*np.pi)+0.7*np.cos(2*np.pi*(1200/fs)*n-4*np.pi) + \
        0.5*np.sin(2*np.pi*(2600/fs)*n)+0.4*np.cos(2*np.pi*(3300/fs)*n)
    discrete_plotter(n, x_n, "Señal Discreta", "Discreta", "Tiempo Discreto", "Amplitud")

    # Transformada de Fourier Índice k vs Amplitud
    X = np.fft.fft(x_n)
    k = np.arange(end_time*fs)
    discrete_plotter(k, np.abs(X), "Transformada de Fourier", "Fourier", "K", "Amplitud")

    # Transformada de Fourier Frecuencia vs Amplitud
    freqs = np.fft.fftfreq(int(end_time*fs), 1/fs)
    discrete_plotter(freqs, np.abs(X), "Transformada de Fourier", "Fourier", "Frecuencia", "Amplitud")

    # Transformada de Fourier Discreta Inversa
    #x_ifft = np.fft.ifft(X).real  # parte real por redondeo numérico
    #discrete_plotter(n, x_ifft, "Reconstrucción IFFT", "IFFT", "n", "Amplitud")