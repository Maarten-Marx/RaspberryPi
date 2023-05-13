import os

import RPi.GPIO as GPIO
from interactions import *
from motor import Motor
from led import LED
from shared import Shared

bot_token = os.getenv("bot-token")
bot = Client(token=bot_token)

motor = Motor(12, 16, 20, 21)
led = LED(18, True)

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
row = ActionRow(components=[close_btn, reset_btn])


@bot.command(
    name="panel",
    description="Opens up a control panel to close or reset the hatch."
)
async def panel(ctx: CommandContext):
    await ctx.send(components=row)


@bot.component("close_btn")
async def close_btn(ctx: ComponentContext):
    state = str(Shared.get_property("state"))

    if state == "Off":
        await ctx.send("The trap is turned off.")
        return

    if state == "Armed":
        await ctx.send("The trap will be closed.")

        Shared.set_property("state", "Closed")
        closed_count = int(Shared.get_property("close_count") or 0)
        Shared.set_property("close_count", closed_count + 1)

        led.set_state(GPIO.HIGH)
        motor.close()
    else:
        await ctx.send("The trap is already closed.")


@bot.component("reset_btn")
async def reset_btn(ctx: ComponentContext):
    state = str(Shared.get_property("state"))

    if state == "Off":
        await ctx.send("The trap is turned off.")
        return

    if state == "Closed":
        await ctx.send("The trap will be reset.")

        Shared.set_property("state", "Armed")

        led.set_state(GPIO.LOW)
        motor.open()
    else:
        await ctx.send("The trap is already reset.")


bot.start()
