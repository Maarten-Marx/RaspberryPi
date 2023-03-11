import time
import RPi.GPIO as GPIO

led_pin = 4
switch_pin = 17
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(switch_pin, GPIO.IN)

sequence = [.5, 1.5, .5]
while True:
    if GPIO.input(switch_pin) == GPIO.LOW:
        for duration in sequence:
            GPIO.output(led_pin, GPIO.HIGH)
            time.sleep(duration)
            GPIO.output(led_pin, GPIO.LOW)
            time.sleep(.5)
    else:
        time.sleep(.5)
