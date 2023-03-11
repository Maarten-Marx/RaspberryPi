import time
import RPi.GPIO as GPIO

trigger_pin = 17
echo_pin = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(trigger_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)

while True:
    GPIO.output(trigger_pin, GPIO.HIGH)
    time.sleep(0.0001)
    GPIO.output(trigger_pin, GPIO.LOW)

    while GPIO.input(echo_pin) == GPIO.LOW:
        pass

    start_time = time.time()
    while GPIO.input(echo_pin) == GPIO.HIGH:
        pass
    end_time = time.time()

    interval = end_time - start_time
    distance = interval * 17000
    print(distance)

    time.sleep(0.5)
