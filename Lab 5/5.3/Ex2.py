import time
import RPi.GPIO as GPIO

sensor_pin = 17
led_pin = 27

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT)

while True:
    if GPIO.input(sensor_pin) == GPIO.HIGH:
        print("Light off")
        GPIO.output(led_pin, GPIO.LOW)
        time.sleep(0.3)
    else:
        print("Light on")
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(0.3)
