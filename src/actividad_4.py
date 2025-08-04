import numpy as np
import matplotlib.pyplot as plt


def aliasing():

    """
        Ejercicio 1
    """
    print("=== Ejercicio 1 ===")

    F0 = 50           # Hz
    fs_min = 2*F0     # Nyquist

    print(f"(a) F0      = {F0} Hz")
    print(f"(b) fs_min  = {fs_min} Hz\n")

    def plot_e1(fs):
        Ts = 1/fs
        t = np.linspace(0, 0.1, 1000)
        n = np.arange(0, 0.1, Ts)
        x_cont = 3*np.cos(2*np.pi*F0*t)
        x_disc = 3*np.cos(2*np.pi*F0*n)
        Fmax = fs/2
        if F0>Fmax:
            fal = abs(F0-round(F0/fs)*fs)
            lab = f"muestra @ {fs} Hz (alias={fal:.1f} Hz)"
        else:
            lab = f"muestra @ {fs} Hz"
        plt.figure(figsize=(6,3))
        plt.plot(t, x_cont, label="continua")
        plt.stem(n, x_disc, basefmt='k-', label=lab)
        plt.title(f"Muestreo a {fs} Hz")
        plt.xlabel("t (s)")
        plt.ylabel("x")
        plt.legend(); plt.grid(True); plt.tight_layout(); plt.show()
        fn = F0/fs
        print(f"→ f_norm={fn:.3f} ciclos/muestra\n")


    plot_e1(200)

    plot_e1(75)

    fal75 = abs(F0-round(F0/75)*75)
    print(f"(e) F_eq en [0,37.5] = {fal75} Hz\n")

    """
        Ejercicio 2
    """
    print("=== Ejercicio 2 ===")

    F0_e2 = 1/8
    F1_e2 = -7/8
    fs2 = 1
    Ts2 = 1/fs2
    t2 = np.linspace(0, 4, 1000)
    n2 = np.arange(0, 4, Ts2)

    # generaciones
    x0c = np.cos(2*np.pi*F0_e2*t2)
    x1c = np.cos(2*np.pi*F1_e2*t2)
    x0d = np.cos(2*np.pi*F0_e2*n2)
    x1d = np.cos(2*np.pi*F1_e2*n2)

    # graficar
    fig, axs = plt.subplots(2, 2, figsize=(8,6), sharex='col')
    axs[0,0].plot(t2, x0c); axs[0,0].set_title("Contínua 1/8 Hz")
    axs[1,0].stem(n2, x0d, basefmt='k-'); axs[1,0].set_title("Muestreada")
    axs[0,1].plot(t2, x1c); axs[0,1].set_title("Contínua –7/8 Hz")
    axs[1,1].stem(n2, x1d, basefmt='k-'); axs[1,1].set_title("Muestreada")
    for ax in axs.flatten():
        ax.grid(True)
        ax.set_ylabel("x")
    axs[1,0].set_xlabel("t (s)")
    axs[1,1].set_xlabel("t (s)")
    plt.tight_layout(); plt.show()

    print("→ Ambas secuencias coinciden: aliasing espectral debido a periodicidad en fs.")
