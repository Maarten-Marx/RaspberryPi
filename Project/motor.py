import time

import RPi.GPIO as GPIO


class Motor:
    def __init__(self, *pins):
        if len(pins) < 4:
            raise Exception("Not enough pins provided. There must be at least 4.")

        self._pins = pins[:4]

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        for p in self._pins:
            GPIO.setup(p, GPIO.OUT)

    def close(self):
        self._turn(self._pins)

    def open(self):
        self._turn(self._pins[::-1])

    @staticmethod
    def _turn(pins: [int]):
        for p in pins:
            GPIO.output(p, GPIO.LOW)

        start_time = time.time()

        while True:
            for idx, pin in enumerate(pins):
                previous = pins[idx - 1]
                turn_off = pins[idx - 2]
                GPIO.output(turn_off, GPIO.LOW)
                GPIO.output(previous, GPIO.HIGH)
                GPIO.output(pin, GPIO.HIGH)
                time.sleep(0.005)

            if time.time() - start_time >= 5.5:
                break
