import time
import RPi.GPIO as GPIO

relay_pins = [4, 5]
switch_pins = [17, 27]
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
for pin in relay_pins:
    GPIO.setup(pin, GPIO.OUT)
for pin in switch_pins:
    GPIO.setup(pin, GPIO.IN)

while True:
    for i in range(2):
        value = GPIO.LOW if GPIO.input(switch_pins[i]) == GPIO.HIGH else GPIO.HIGH  # active low
        GPIO.output(relay_pins[i], value)

    time.sleep(.1)
