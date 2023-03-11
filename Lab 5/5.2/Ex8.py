import time
import RPi.GPIO as GPIO

pins = range(4, 8)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

delay = .01

while True:
    for idx, pin in enumerate(pins):
        previous = pins[idx - 1]
        turn_off = pins[idx - 2]
        GPIO.output(turn_off, GPIO.LOW)
        GPIO.output(previous, GPIO.HIGH)
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(delay)
