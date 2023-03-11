import time
import RPi.GPIO as GPIO

pins = range(4, 8)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

while True:
    for idx, pin in enumerate(pins):
        previous = pins[idx - 1]
        GPIO.output(previous, GPIO.LOW)
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(.1)
