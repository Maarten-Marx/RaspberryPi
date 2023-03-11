import time
import RPi.GPIO as GPIO

switch_pin = 17

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(switch_pin, GPIO.IN)

while True:
    if GPIO.input(switch_pin) == 0:
        print("Button pressed")
        time.sleep(0.3)
    else:
        print("Button released")
        time.sleep(0.3)
