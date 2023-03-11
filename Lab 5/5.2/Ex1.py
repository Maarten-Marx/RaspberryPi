import time
import RPi.GPIO as GPIO


def blink(_pin):
    GPIO.output(_pin, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(_pin, GPIO.LOW)
    time.sleep(0.5)


led_pin = 4
switch_pin = 17
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(switch_pin, GPIO.IN)

while True:
    if GPIO.input(switch_pin) == GPIO.LOW:
        print("LED blinking")
        blink(led_pin)
    else:
        print("LED off")
        time.sleep(1)
