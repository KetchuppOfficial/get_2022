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

    for val in range(levels):

        signal = dtob (val)
        RT.output (dac, signal)

        time.sleep (0.0001)

        comp_val = RT.input (comp)
        if comp_val == 0:
            return val

    return 0

try:
        while 1:
            val = adc ()
            print ("ADC value = {:^3}, input voltage = {:.2f}".format (val, val / levels * V_max))

except KeyboardInterrupt:
    print ("\nProgram stopped by keyboard\n")

else:
    print ("No exceptions")

finally:
    RT.output  (dac, 0)
    RT.cleanup (dac)