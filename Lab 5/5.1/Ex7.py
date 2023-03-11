import time
import RPi.GPIO as GPIO

led_pin = 4
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)


def blink(pin, blink_count, period, duty_cycle):
    time_high = period * duty_cycle / 100
    time_low = period - time_high
    for i in range(blink_count):
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(time_high)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(time_low)


blink(led_pin, 20, .5, 75)

print("Done")
