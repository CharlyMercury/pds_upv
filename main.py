import sys
from src.actividad_1 import continuous_sine, discrete_sine
from src.actividad_2 import understanding_freq
from src.actividad_3 import muestreo
from src.actividad_4 import aliasing

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


if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        main(args)
    else:
        print("Please give an argument")
        print("Example ( run activity 1 ) : python main.py act_1")
        print("Example ( run activity 2 ) : python main.py act_2 1")
        print("Example ( run muestreo ) : python main.py muestreo f1 f2 fs duración")


"""

python main.py muestreo 5 15 50 1.0
python main.py muestreo 10 30 40 0.5
python main.py muestreo 45 70 60 0.25
python main.py muestreo 18 22 100 0.75

python main.py aliasing
"""
