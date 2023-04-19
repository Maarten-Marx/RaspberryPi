import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)

led1 = GPIO.PWM(7, 100)
led2 = GPIO.PWM(8, 100)

led1.start(0)
led2.start(100)

pause_time = 0.01

while True:
    for i in range(0, 101):
        led1.ChangeDutyCycle(i)
        led2.ChangeDutyCycle(100 - i)
        time.sleep(pause_time)

    for i in range(100, -1, -1):
        led1.ChangeDutyCycle(i)
        led2.ChangeDutyCycle(100 - i)
        time.sleep(pause_time)
