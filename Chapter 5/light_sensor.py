import time
import RPi.GPIO as GPIO

sensor_pin = 17

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN)

while True:
    if GPIO.input(sensor_pin) == 1:
        print("Light")
        time.sleep(0.3)
    else:
        print("Dark")
        time.sleep(0.3)
