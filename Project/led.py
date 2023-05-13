import RPi.GPIO as GPIO


# Simple class for controlling LEDs
class LED:
    def __init__(self, pin, active_low: bool):
        # Store the pin number, and whether it's active-low or not
        self._pin = pin
        self._active_low = active_low

        # GPIO and pin setup
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self._pin, GPIO.OUT)

    def set_state(self, state: int):
        # Invert input when active-low
        if self._active_low:
            state = abs(state - 1)
        GPIO.output(self._pin, state)
