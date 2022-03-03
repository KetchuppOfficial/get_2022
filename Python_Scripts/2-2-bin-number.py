import RPi.GPIO as RTRTRT
import time
import random

dac    = [26, 19, 13, 6, 5, 11, 9, 10]

number = [0, 0, 0, 0, 0, 1, 0, 1]
RTRTRT.setmode(RTRTRT.BCM)

RTRTRT.setup (dac, RTRTRT.OUT)

#for num in range(8):
#    number.append(random.randint(0, 1))

RTRTRT.output (dac, number)

time.sleep (15)

RTRTRT.output (dac, 0)
RTRTRT.cleanup ()