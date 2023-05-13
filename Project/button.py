import RPi.GPIO as GPIO


class Button:
    def __init__(self, pin):
        self._pin = pin

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self._pin, GPIO.IN)

    def pressed(self):
        return GPIO.input(self._pin) == GPIO.LOW
