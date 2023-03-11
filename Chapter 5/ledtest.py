import time
import RPi.GPIO as GPIO


def blink(_pin):
    GPIO.output(_pin, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(_pin, GPIO.LOW)
    time.sleep(0.5)


# SETUP
print('Start')
pin = 4
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

# MAIN
for i in range(10):
    blink(pin)

# Cleanup
print('Done')
