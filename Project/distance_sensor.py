import time

import RPi.GPIO as GPIO


class DistanceSensor:
    def __init__(self, trigger: int, echo: int):
        self._trigger_pin = trigger
        self._echo_pin = echo

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self._trigger_pin, GPIO.OUT)
        GPIO.setup(self._echo_pin, GPIO.IN)

    def measure(self):
        GPIO.output(self._trigger_pin, GPIO.HIGH)
        time.sleep(0.0001)
        GPIO.output(self._trigger_pin, GPIO.LOW)

        while GPIO.input(self._echo_pin) == GPIO.LOW:
            pass

        start_time = time.time()
        while GPIO.input(self._echo_pin) == GPIO.HIGH:
            pass
        end_time = time.time()

        interval = end_time - start_time
        return interval * 17000
