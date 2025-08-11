import sys
from src.actividad_1 import continuous_sine, discrete_sine
from src.actividad_2 import understanding_freq
from src.actividad_3 import muestreo
from src.actividad_4 import aliasing
from src.actividad_5 import reconstruction
from src.ejemplo_dft_1 import dft_1
from src.ejemplo_dft_2 import dft_2
from src.ejemplo_dft_3 import dft_3
from src.charly_dft import discretization

def main(options):
    if options[1] == "act_1":
        continuous_sine()
        discrete_sine()
    elif options[1] == "act_2":
        if len(args) > 2:
            understanding_freq(options[2])
        else:
            print("Please give a frequency. Example: python main.py act_2 2")
    elif options[1] == "muestreo":
        if len(args) > 4:
            f1 = int(options[2])
            f2 = int(options[3])
            fs = int(options[4])
            duration = float(options[5])
            muestreo(f1, f2, fs, duration)
    elif options[1] == "aliasing":
        if len(args) > 1:
            aliasing()
    elif options[1] == "reconstruction":
        if len(args) > 2:
            fs = int(options[2])
            # Función coseno 
            F0 = 15  # Frecuencia de mi señal (función coseno)
            A = 1.5  # Amplitud
            reconstruction(F0, A, fs)
    elif options[1] == "dft_1":
        if len(args) > 1:
            dft_1()
    elif options[1] == "dft_2":
        if len(args) > 1:
            dft_2()
    elif options[1] == "dft_3":
        if len(args) > 3:
            m = int(options[2])
            N = int(options[3])
            dft_3(m, N)
        else:
            print("Please give an index and Samples. Example: python main.py dft_2 1 32")
    elif options[1] == "dft_ch":
        if len(args) > 1:
            discretization(0.001, 8000)
            #dft_charly([1, 2, 3, 4, 5])
    else:
        print("Opción inválida")


if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        main(args)
    else:
        print("Please give an argument")
        print("Example ( run activity 1 ) : python main.py act_1")
        print("Example ( run activity 2 ) : python main.py act_2 1")
        print("Example ( run muestreo ) : python main.py muestreo f1 f2 fs duración")
        print("Example ( run reconstruction ) : python main.py reconstruction 30")
        print("Example ( run reconstruction ) : python main.py reconstruction 30")
        print("Example ( run dft1 ) : python main.py dft_1")
        print("Example ( run dft2 ) : python main.py dft_2")
        print("Example ( run dft3 ) : python main.py dft_3 m N")  # m indice de la DFT y N número de muestras
        print("Example ( run dft ch ) : python main.py dft_ch")  # m indice de la DFT y N número de muestras


"""

python main.py muestreo 5 15 50 1.0
python main.py muestreo 10 30 40 0.5
python main.py muestreo 45 70 60 0.25
python main.py muestreo 18 22 100 0.75

python main.py aliasing
"""
