import RPi.GPIO as RT
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]

RT.setmode(RT.BCM)
RT.setup (dac, RT.OUT)

def dtob(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

try:
    while 1:
        T = float (input ("Write saw period: "))
    
        t = T/256

        while (1):
            for i in range (0, 255):
                RT.output (dac, dtob(i))
                time.sleep(t)
            for i in range (255, 0, -1):
                RT.output (dac, dtob(i))
                time.sleep(t)

except ValueError:
    print ("Incorrect data")

    
finally:
    RT.output (dac, 0)
    RT.cleanup ()