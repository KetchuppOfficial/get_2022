import RPi.GPIO as RTRTRT
import time

leds = [21, 20, 16, 12, 7, 8, 25, 24]

RTRTRT.setmode(RTRTRT.BCM)

RTRTRT.setup (leds, RTRTRT.OUT)

for circle in range (3):
    for lamp_i in leds:
        RTRTRT.output (lamp_i, 1)
        time.sleep(0.2)
        RTRTRT.output (lamp_i, 0)

RTRTRT.output (leds, 0)

RTRTRT.cleanup()
