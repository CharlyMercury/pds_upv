import numpy as np
import matplotlib.pyplot as plt

def reconstruction(F0, A, fs, duration = 1.0):
    # Parámetros de la señal original
    phi = 0.0
    duration = 1.0

    # Parámetros de muestreo
    freq_nyquist = 2*F0      # Frecuencia de Nyquist
    print(f"Frecuencia de muestreo {freq_nyquist}")
    ts = 1.0 / fs  # Periodo de muestreo

    if fs < freq_nyquist:
        print("Aliasing")
    else:
        print("Good Job")

    # Variables independientes
    t_cont = np.linspace(0, duration, 20000)  
    n = np.arange(0, duration, ts)

    # Señal continua
    x_cont = A * np.cos(2 * np.pi * F0 * t_cont + phi)
    # Señal discreta
    x_disc = A * np.cos(2 * np.pi * F0 * n + phi)

    # Reconstrucción por interpolación sinc
    t_rec = t_cont.copy()
    x_rec = np.zeros_like(t_rec)
    for k, xk in enumerate(x_disc):
        # Señal reconstruida
        x_rec += xk * np.sinc((t_rec - k*ts) / ts)

    # Gráfica
    plt.figure(figsize=(8, 4))
    plt.plot(t_cont, x_cont, 'k-', label='Señal continua')
    markerline, stemlines, baseline = plt.stem(
        n, x_disc, linefmt='r-', markerfmt='ro', basefmt='k-', label='Muestras discretas'
    )
    plt.setp(markerline, markersize=6)
    plt.setp(stemlines, linewidth=1)
    plt.plot(t_rec, x_rec, 'b--', label='Reconstrucción sinc')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.title('Reconstrucción de señal mediante sinc-interpolación')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
