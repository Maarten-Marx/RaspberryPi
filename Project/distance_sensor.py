import time

import RPi.GPIO as GPIO


# Class for controlling the distance sensor
class DistanceSensor:
    def __init__(self, trigger: int, echo: int):
        # Store the pin numbers from the parameters
        self._trigger_pin = trigger
        self._echo_pin = echo

        # GPIO and pin setup
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self._trigger_pin, GPIO.OUT)
        GPIO.setup(self._echo_pin, GPIO.IN)

    def measure(self):
        # Send a pulse
        GPIO.output(self._trigger_pin, GPIO.HIGH)
        time.sleep(0.0001)
        GPIO.output(self._trigger_pin, GPIO.LOW)

        # Measure the time between the transmission and the response
        while GPIO.input(self._echo_pin) == GPIO.LOW:
            pass

        start_time = time.time()
        while GPIO.input(self._echo_pin) == GPIO.HIGH:
            pass
        end_time = time.time()

        # Calculate distance based on the time it took for the sound to get back to the sensor
        interval = end_time - start_time
        return interval * 17000
