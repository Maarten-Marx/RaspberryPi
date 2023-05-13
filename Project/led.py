import RPi.GPIO as GPIO


class LED:
    def __init__(self, pin, active_low: bool):
        self._pin = pin
        self._active_low = active_low

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self._pin, GPIO.OUT)

    def set_state(self, state: int):
        if self._active_low:
            state = abs(state - 1)
        GPIO.output(self._pin, state)
