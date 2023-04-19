import board
import busio
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_pcd8544
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17, GPIO.IN)
GPIO.setup(4, GPIO.IN)

spi = busio.SPI(board.SCK, MOSI=board.MOSI)
dc = digitalio.DigitalInOut(board.D6)
cs = digitalio.DigitalInOut(board.CE1)
reset = digitalio.DigitalInOut(board.D5)

display = adafruit_pcd8544.PCD8544(spi, dc, cs, reset)

FONTSIZE = 10

display.bias = 4
display.contrast = 60

display.fill(0)
display.show()


def get_name():
    current = os.popen("mpc current").readlines()[0]
    station = current.split("/")[-1]
    name = station.split("-")[0]
    return name


def show_station():
    image = Image.new("1", (display.width, display.height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", FONTSIZE)

    draw.text((0, 0), "Now playing:", font=font, fill=255)
    draw.text((0, 10), get_name(), font=font, fill=255)

    display.image(image)
    display.show()


# to prevent subsequent station changes when the buttons are held
prev_was_pressed = False
next_was_pressed = False

os.system("mpc play")
show_station()

while True:
    if not next_was_pressed and GPIO.input(17) == 0:
        os.system("mpc next")
        # mpc stops playing when the end of the playlist is reached
        # output to /dev/null to prevent double logging
        os.system("mpc play > /dev/null")
        show_station()
        next_was_pressed = True
    elif GPIO.input(17) == 1:
        next_was_pressed = False

    if not prev_was_pressed and GPIO.input(4) == 0:
        os.system("mpc prev")
        show_station()
        prev_was_pressed = True
    elif GPIO.input(4) == 1:
        prev_was_pressed = False
