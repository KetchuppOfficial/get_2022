import RPi.GPIO as RTRTRT

RTRTRT.setmode(RTRTRT.BCM)

RTRTRT.setup(14, RTRTRT.OUT)
RTRTRT.setup(15, RTRTRT.IN)

print ("Hello, malina")
RTRTRT.output(14, RTRTRT.input(15))