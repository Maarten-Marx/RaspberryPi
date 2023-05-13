import os

import RPi.GPIO as GPIO
from interactions import *
from motor import Motor
from led import LED
from shared import Shared

# Get the bot token from an environment variable, so it's not visible in the source code
bot_token = os.getenv("bot-token")
# Create a Discord bot
bot = Client(token=bot_token)

# Set up the motor and LED for the Discord bot to control
motor = Motor(12, 16, 20, 21)
led = LED(18, True)

# Define buttons that are sent alongside the response to the /panel command
close_btn = Button(
    label="Close Trap",
    style=ButtonStyle.DANGER,
    custom_id="close_btn"
)
reset_btn = Button(
    label="Reset Trap",
    style=ButtonStyle.SUCCESS,
    custom_id="reset_btn"
)
# Store the buttons in a row that can be sent alongside a message
row = ActionRow(components=[close_btn, reset_btn])


# Define the /panel command
@bot.command(
    name="panel",
    description="Opens up a control panel to close or reset the hatch."
)
async def panel(ctx: CommandContext):
    # Send a message with 2 buttons
    await ctx.send(components=row)


# Define the event handler for the "Close Trap" button
@bot.component("close_btn")
async def close_btn(ctx: ComponentContext):
    # Get the current state from the data shared between the bot and the main script
    state = str(Shared.get_property("state"))

    if state == "Off":
        # Don't close the hatch when the trap is turned off
        await ctx.send("The trap is turned off.")
        return

    if state == "Armed":
        # Only close the trap when it's armed
        await ctx.send("The trap will be closed.")

        # Save the new state and close-count to the shared data
        Shared.set_property("state", "Closed")
        closed_count = int(Shared.get_property("close_count") or 0)
        Shared.set_property("close_count", closed_count + 1)

        # Turn on the LED and turn the motor
        led.set_state(GPIO.HIGH)
        motor.close()
    else:
        # Don't close the hatch when the trap is already closed
        await ctx.send("The trap is already closed.")


@bot.component("reset_btn")
async def reset_btn(ctx: ComponentContext):
    # Get the current state from the data shared between the bot and the main script
    state = str(Shared.get_property("state"))

    if state == "Off":
        # Don't open the hatch when the trap is turned off
        await ctx.send("The trap is turned off.")
        return

    if state == "Closed":
        # Only open the trap when it's closed
        await ctx.send("The trap will be reset.")

        # Save the new state to the shared data
        Shared.set_property("state", "Armed")

        # Turn off the LED and turn the motor
        led.set_state(GPIO.LOW)
        motor.open()
    else:
        # Don't open the hatch when the trap is already open
        await ctx.send("The trap is already reset.")

# Start the bot
bot.start()
