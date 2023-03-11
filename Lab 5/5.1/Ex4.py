import time
import RPi.GPIO as GPIO

pins = range(4, 8)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

step = 1
idx = 0
while True:
    previous = pins[idx - step]
    GPIO.output(previous, GPIO.LOW)
    current = pins[idx]
    GPIO.output(current, GPIO.HIGH)

    if idx == len(pins) - 1:
        step = -1
    elif idx == 0:
        step = 1
    idx += step

    time.sleep(.1)
