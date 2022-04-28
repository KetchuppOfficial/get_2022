import RPi.GPIO as RT
import time
import matplotlib.pyplot as plt

dac    = [26, 19, 13,  6, 5, 11,  9, 10]
leds   = [21, 20, 16, 12, 7,  8, 25, 24]
comp   = 4
troyka = 17

bits   = len (dac)
levels = 2**bits
V_max  = 255

RT.setmode (RT.BCM)

RT.setup (leds, RT.OUT)
RT.setup (dac, RT.OUT)
RT.setup (troyka, RT.OUT, initial = 1)
RT.setup (comp, RT.IN)

def dtob (value):
    return [int(element) for element in bin(value)[2:].zfill(bits)]

def Get_Voltage ():

    signal = [0, 0, 0, 0, 0, 0, 0, 0] 
    voltage = 0

    for i in range(8):

        signal[i] = 1
        RT.output (dac, signal)

        time.sleep (0.0005)

        comp_val = RT.input (comp)
        signal[i] = comp_val

        voltage = voltage + 2**(7 - i)*comp_val

    return voltage

def Let_There_Be_More_Light (voltage):
    RT.output (leds, dtob(voltage))

try:
    measures = []
    n_experiments = 0
    start_up = time.time()

    RT.output(troyka, 1)

    voltage = 0
    while voltage < 0.97 * V_max:
        voltage = Get_Voltage()
        Let_There_Be_More_Light (voltage)
        measures.append(voltage)
        print ('voltage = {}'.format(voltage))
        n_experiments += 1

    start_down = time.time()
    RT.output(troyka, 0)

    while voltage > 0.02 * V_max:
        voltage = Get_Voltage()
        Let_There_Be_More_Light (voltage)
        measures.append(voltage)
        print ('voltage = {}'.format(voltage))
        n_experiments += 1

    stop = time.time()

    time_up = start_down - start_up
    time_down = stop - start_down
    time_whole = stop - start_up

    plt.plot(measures)
    plt.savefig('Graph.png')

    measures_str = [str(item) for item in measures]

    step = 3.3 / levels

    with open('data.txt', 'w') as data:
        data.write("\n".join(measures_str))

    with open('settings.txt', 'w') as settings:
        settings.write('Средняя частота дискретизации проведённых измерений: {:.2f}\n'.format(n_experiments/time_whole))
        settings.write('Шаг квантования АЦП: {:.2}'.format(step))

    print ('Время эксперимента: {:.2f}'.format(time_whole))
    print ('Период одного измерения: {:.3f}'.format(time_whole/n_experiments))
    print ('Средняя частота дискретизации проведённых измерений: {:.2f}'.format(n_experiments/time_whole))
    print ('Шаг квантования АЦП: {:.2}'.format(step))
except KeyboardInterrupt:
    print ("\nProgram stopped by keyboard\n")

else:
    print ("No exceptions")

finally:
    RT.cleanup ()