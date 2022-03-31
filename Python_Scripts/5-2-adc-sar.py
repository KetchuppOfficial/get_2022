import RPi.GPIO as RT
import time

dac    = [26, 19, 13, 6, 5, 11, 9, 10]
comp   = 4
troyka = 17

bits   = len (dac)
levels = 2**bits
V_max  = 3.3

RT.setmode (RT.BCM)
RT.setup (dac, RT.OUT)

RT.setup (troyka, RT.OUT, initial = 1)

RT.setup (comp, RT.IN)

def dtob (value):
    return [int(element) for element in bin(value)[2:].zfill(bits)]

def adc ():

    signal = [0, 0, 0, 0, 0, 0, 0, 0] 
    voltage = 0

    for i in range(8):

        signal[i] = 1
        RT.output (dac, signal)

        time.sleep (0.0005)

        comp_val = RT.input (comp)
        signal[i] = comp_val
        voltage = voltage + 2**(7 - i)*comp_val

    #print ("MASSIVE: {}".format (signal))

    return voltage

try:
        while 1:
            print ("Input voltage = {:.2f}".format (adc () / levels * V_max))

except KeyboardInterrupt:
    print ("\nProgram stopped by keyboard\n")

else:
    print ("No exceptions")

finally:
    RT.output  (dac, 0)
    RT.cleanup (dac)