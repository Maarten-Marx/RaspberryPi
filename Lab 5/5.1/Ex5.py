import time
import RPi.GPIO as GPIO

pins = range(4, 8)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

while True:
    for idx in range(2):
        previous_idx = (idx + 1) % 2  # 1 stays 1, 2 becomes 0
        previous = pins[previous_idx::2]
        for pin in previous:
            GPIO.output(pin, GPIO.LOW)

        current = pins[idx::2]
        for pin in current:
            GPIO.output(pin, GPIO.HIGH)

        time.sleep(1)
