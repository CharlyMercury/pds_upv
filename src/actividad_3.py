# src/actividad_3.py
import numpy as np
import matplotlib.pyplot as plt

def muestreo(f1, f2, fs, duration):
    """
    Grafica dos señales (f1, f2) en tiempo continuo y muestreado,
    usando subplots comparativos para cada frecuencia y mostrando aliasing de Nyquist.

    Parámetros:
    - f1, f2: frecuencias de las señales (Hz)
    - fs: frecuencia de muestreo (Hz)
    - duration: duración de la señal en segundos
    """
    # Definir periodo y vectores de tiempo
    Ts = 1 / fs
    t = np.linspace(0, duration, 1000)
    n = np.arange(0, duration, Ts)

    # Señales continuas
    x1_cont = np.cos(2 * np.pi * f1 * t)
    x2_cont = np.cos(2 * np.pi * f2 * t)

    # Señales muestreadas
    x1_disc = np.cos(2 * np.pi * f1 * n)
    x2_disc = np.cos(2 * np.pi * f2 * n)

    # Frecuencia de Nyquist
    F_max = fs / 2
    print(f"Frecuencia de Nyquist (fs/2): {F_max:.2f} Hz")

    # Cálculo de alias para f1
    if f1 > F_max:
        m1 = round(f1 / fs)
        alias1 = abs(f1 - m1 * fs)
    else:
        alias1 = None

    # Cálculo de alias para f2
    if f2 > F_max:
        m2 = round(f2 / fs)
        alias2 = abs(f2 - m2 * fs)
    else:
        alias2 = None

    # Crear subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)

    # Primer subplot: f1
    ax1.plot(t, x1_cont, label=f'{f1} Hz (continua)')
    label_disc1 = f'fs {fs} Hz'
    if alias1:
        label_disc1 += f' (alias={alias1:.1f} Hz)'
    ax1.stem(n, x1_disc, label=label_disc1)
    ax1.set_title(f'Señal de {f1} Hz')
    ax1.set_ylabel('Amplitud')
    ax1.legend()
    ax1.grid(True)

    # Segundo subplot: f2
    ax2.plot(t, x2_cont, label=f'{f2} Hz (continua)')
    label_disc2 = f'fs - {fs} Hz'
    if alias2:
        label_disc2 += f' (alias={alias2:.1f} Hz)'
    ax2.stem(n, x2_disc, label=label_disc2)
    ax2.set_title(f'Señal de {f2} Hz')
    ax2.set_xlabel('Tiempo (s)')
    ax2.set_ylabel('Amplitud')
    ax2.legend()
    ax2.grid(True)

    plt.tight_layout()
    plt.show()
