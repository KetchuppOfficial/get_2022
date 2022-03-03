import RPi.GPIO as RTRTRT

leds = [21, 20, 16, 12,  7,  8, 25, 24]
aux  = [22, 23, 27, 18, 15, 14, 13, 2]

RTRTRT.setmode(RTRTRT.BCM)
RTRTRT.setup (leds, RTRTRT.OUT)
RTRTRT.setup (aux, RTRTRT.IN)

try:
    while 1:
        for lamp_i in range (8):
            RTRTRT.output (leds[lamp_i], RTRTRT.input (aux[lamp_i]))
finally:
    RTRTRT.output (leds, 0)
    RTRTRT.cleanup()