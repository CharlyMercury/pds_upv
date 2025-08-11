import numpy as np


def dft_3(m, N):

    n = np.arange(N)

    x_n = np.cos(2*np.pi*(3/N)*n) - np.sin(2*np.pi*(10/N)*n)

    re = np.sum(x_n*np.cos(2*np.pi*m*n/N))
    im = np.sum(x_n*np.sin(2*np.pi*m*n/N))

    print(f"Parte Real: {re}")
    print(f"Parte Imaginaria: {im}")