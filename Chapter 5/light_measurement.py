import time
import RPi.GPIO as GPIO

capacitor_pin = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

while True:
    GPIO.setup(capacitor_pin, GPIO.OUT)
    GPIO.output(capacitor_pin, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(capacitor_pin, GPIO.IN)
    start_time = time.time()

    while GPIO.input(capacitor_pin) == GPIO.LOW:
        pass

    end_time = time.time()
    interval = int((end_time - start_time) * 1_000_000)

    print(interval)
