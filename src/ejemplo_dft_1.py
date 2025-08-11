import numpy as np
from src.utils.grapher import continuous_plotter, discrete_plotter


def dft_1():

    end_time = 0.05

    # Graficamos la señal continua
    t = np.linspace(0, end_time, 10000)
    x_t = 1.2*np.cos(2*np.pi*750*t) +0.8*np.cos(2*np.pi*2200*t)
    + 0.4*np.cos(2*np.pi*3500*t)
    continuous_plotter(t, x_t, "Señal continua", "continua", "Tiempo [S]", "Amplitud ")

    # Graficamos la señal discreta
    fs = 8000
    n = np.arange(end_time*fs)
    x_n = 1.2*np.cos(2*np.pi*(750/fs)*n) +0.8*np.cos(2*np.pi*(2200/fs)*n) + 0.4*np.cos(2*np.pi*(3500/fs)*n)
    discrete_plotter(n, x_n, "Señal discreta", "discreta", "Tiempo [n*ts]", "Amplitud ")

    # Calculamos y graficamos la amplitud de la DFT
    X = np.fft.fft(x_n)
    k = np.arange(end_time*fs)
    discrete_plotter(k, np.abs(X), "Transformada de Fourier Discreta", "discreta", "k (índice de frecuencia)", "Amplitud ")

    # Calculamos y graficamos la freq vs la amplitud de la DFT
    freqs = np.fft.fftfreq(int(end_time*fs), 1/fs)
    discrete_plotter(freqs, np.abs(X), "Transformada de Fourier Discreta", "discreta", "Frecuencia", "Amplitud ")

