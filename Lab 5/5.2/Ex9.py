import time
import RPi.GPIO as GPIO

motor_pins = range(4, 8)
switch_pin = 17
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
for pin in motor_pins:
    GPIO.setup(pin, GPIO.OUT)
GPIO.setup(switch_pin, GPIO.IN)

delay = .01

while True:
    pin_order = list(motor_pins if GPIO.input(switch_pin) == GPIO.LOW else reversed(motor_pins))
    for idx, pin in enumerate(pin_order):
        previous = pin_order[idx - 1]
        GPIO.output(previous, GPIO.LOW)
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(delay)
