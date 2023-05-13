import RPi.GPIO as GPIO


# Simple class for reading button input
class Button:
    def __init__(self, pin):
        # Store the pin number
        self._pin = pin

        # GPIO and pin setup
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self._pin, GPIO.IN)

    def pressed(self):
        # All buttons in this setup are active-low
        return GPIO.input(self._pin) == GPIO.LOW
