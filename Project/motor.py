import time

import RPi.GPIO as GPIO


# Class for controlling the motor
class Motor:
    def __init__(self, *pins):
        # Throw an error when not enough pins are provided
        if len(pins) < 4:
            raise Exception("Not enough pins provided. There must be at least 4.")

        # Store the first 4 provided pins
        self._pins = pins[:4]

        # GPIO and pin setup
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        for p in self._pins:
            GPIO.setup(p, GPIO.OUT)

    def close(self):
        # Turn the motor with the standard pin order
        self._turn(self._pins)

    def open(self):
        # Turn the motor with the reversed pin order
        self._turn(self._pins[::-1])

    # Common method for turning the motor based on pin numbers
    @staticmethod
    def _turn(pins: [int]):
        # Furn off all pins in case some were left on
        for p in pins:
            GPIO.output(p, GPIO.LOW)

        # Store the start time in order to measure how much time has passed
        start_time = time.time()

        while True:
            # Iterate over the list of pins, turn on or off the appropriate pins
            for idx, pin in enumerate(pins):
                previous = pins[idx - 1]
                turn_off = pins[idx - 2]
                GPIO.output(turn_off, GPIO.LOW)
                GPIO.output(previous, GPIO.HIGH)
                GPIO.output(pin, GPIO.HIGH)
                time.sleep(0.005)

            # Stop turning after 5.5 seconds. This time is equivalent to about 180 degrees of rotation
            if time.time() - start_time >= 5.5:
                break
