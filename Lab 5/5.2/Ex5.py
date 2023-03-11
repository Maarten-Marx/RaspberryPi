import time
import RPi.GPIO as GPIO

led_pins = range(4, 8)
switch_pin = 17
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)
GPIO.setup(switch_pin, GPIO.IN)

while True:
    pin_order = list(led_pins if GPIO.input(switch_pin) == GPIO.LOW else reversed(led_pins))

    for idx, pin in enumerate(pin_order):
        previous = pin_order[idx - 1]
        GPIO.output(previous, GPIO.LOW)
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(.1)
