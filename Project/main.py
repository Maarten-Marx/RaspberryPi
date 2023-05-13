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

# get uBeac info from environment variables, so they're not visible in the source code
UBEAC_URL = os.getenv("UBEAC-URL")
UBEAC_UID = os.getenv("UBEAC-UID")

# Exit the program if required info is missing
if UBEAC_URL is None:
    print("UBEAC_URL environment variable is not set")
    exit(1)

if UBEAC_UID is None:
    print("UBEAC_UID environment variable is not set")
    exit(1)

# Create all objects for interactive with different components
display = Display()
motor = Motor(12, 16, 20, 21)
led = LED(18, True)
power_button = Button(19)
close_button = Button(26)
open_button = Button(13)
ds = DistanceSensor(17, 27)
ubeac = UBeac(UBEAC_URL, UBEAC_UID)

# Reset the close-counter
Shared.set_property("close_count", 0)

# Store the current state as a backup for when the trap is turned off
# When turned back on, this state will be restored
prev_state = str(Shared.get_property("state"))

while True:
    # Fetch shared info that could have been changed by the Discord bot
    close_count = int(Shared.get_property("close_count"))
    state = str(Shared.get_property("state"))

    # Display the current time, state, and close-count
    display.print_lines(
        datetime.now().time().strftime("%H:%M:%S"),
        state,
        f"Closed {close_count} time" + ("" if close_count == 1 else "s")
    )

    # Measure the distance to the closest object in the trap
    measurement = ds.measure()
    ubeac.send_data("trap distance", measurement)

    # Turn on or off the trap, then wait until the button is released before looping again
    if power_button.pressed():
        if state == "Off":
            Shared.set_property("state", prev_state)
        else:
            prev_state = state
            Shared.set_property("state", "Off")

        # Prevent changing the state multiple times while the button is held
        while power_button.pressed():
            pass

    # Close the trap if it is armed, and either of the following happens:
    # - The distance sensor detects something at a distance of less that 7cm
    # - The close button is pressed
    if state == "Armed" and (measurement < 7 or close_button.pressed()):
        # Modify shared information
        Shared.set_property("state", "Closed")
        Shared.set_property("close_count", close_count + 1)

        # Turn on the LED and turn the motor
        led.set_state(GPIO.HIGH)
        motor.close()
    # Open the trap if it is closed, and the open button is pressed
    if state == "Closed" and open_button.pressed():
        # Modify shared information
        Shared.set_property("state", "Armed")

        # Turn off the LED and turn the motor
        led.set_state(GPIO.LOW)
        motor.open()

    # What for a short amount of time before repeating all the previous steps
    time.sleep(.05)
