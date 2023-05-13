import os
import time
import RPi.GPIO as GPIO
from datetime import datetime
from display import Display
from motor import Motor
from led import LED
from button import Button
from distance_sensor import DistanceSensor
from ubeac import UBeac
from shared import Shared

UBEAC_URL = os.getenv("UBEAC-URL")
UBEAC_UID = os.getenv("UBEAC-UID")

if UBEAC_URL is None:
    print("UBEAC_URL environment variable is not set")
    exit(1)

if UBEAC_UID is None:
    print("UBEAC_UID environment variable is not set")
    exit(1)

display = Display()
motor = Motor(12, 16, 20, 21)
led = LED(18, True)
power_button = Button(19)
close_button = Button(26)
open_button = Button(13)
ds = DistanceSensor(17, 27)
ubeac = UBeac(UBEAC_URL, UBEAC_UID)

enabled = True

Shared.set_property("close_count", 0)

prev_state = str(Shared.get_property("state"))

while True:
    close_count = int(Shared.get_property("close_count"))
    state = str(Shared.get_property("state"))

    display.print_lines(
        datetime.now().time().strftime("%H:%M:%S"),
        state,
        f"Closed {close_count} time" + ("" if close_count == 1 else "s")
    )

    measurement = ds.measure()
    ubeac.send_data("trap distance", measurement)

    if power_button.pressed():
        if state == "Off":
            Shared.set_property("state", prev_state)
        else:
            prev_state = state
            Shared.set_property("state", "Off")

        while power_button.pressed():
            pass

    if state == "Armed" and (measurement < 7 or close_button.pressed()):
        Shared.set_property("state", "Closed")
        Shared.set_property("close_count", close_count + 1)

        led.set_state(GPIO.HIGH)
        motor.close()
    if state == "Closed" and open_button.pressed():
        Shared.set_property("state", "Armed")

        led.set_state(GPIO.LOW)
        motor.open()

    time.sleep(.05)
