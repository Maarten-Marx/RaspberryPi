import time
import RPi.GPIO as GPIO
import os
import requests

URL = os.getenv("UBEAC_URL")
UID = os.getenv("UBEAC_UID")

if URL is None:
    print("UBEAC_URL environment variable is not set")
    exit(1)

if UID is None:
    print("UBEAC_UID environment variable is not set")
    exit(1)

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

    data = {
        "id": UID,
        "sensors": [{
            "id": "light level",
            "data": percentage
        }]
    }

    r = requests.post(URL, json=data)
