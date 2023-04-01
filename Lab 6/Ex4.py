import time
import RPi.GPIO as GPIO

capacitor_pin = 17

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

while True:
    GPIO.setup(capacitor_pin, GPIO.OUT)
    GPIO.output(capacitor_pin, GPIO.LOW)
    time.sleep(1)

    GPIO.setup(capacitor_pin, GPIO.IN)
    start_time = time.time()

    while GPIO.input(capacitor_pin) == GPIO.LOW:
        pass

    end_time = time.time()
    # interval in ms
    interval = (end_time - start_time) * 1000

    # An interval of 20ms for complete darkness, 0ms for bright light
    percentage = int(max(15 - interval, 0) / 15 * 100)

    print(f"{percentage}%")
