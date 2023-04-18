# Partially taken from https://learn.adafruit.com/nokia-5110-3310-monochrome-lcd/python-usage#example-code-3044546

import board
import busio
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_pcd8544

spi = busio.SPI(board.SCK, MOSI=board.MOSI)
dc = digitalio.DigitalInOut(board.D6)  # data/command
cs = digitalio.DigitalInOut(board.CE0)  # Chip select
reset = digitalio.DigitalInOut(board.D5)  # reset

display = adafruit_pcd8544.PCD8544(spi, dc, cs, reset)

FONTSIZE = 10

display.bias = 5
display.contrast = 50

backlight = digitalio.DigitalInOut(board.D13)  # backlight
backlight.switch_to_output()
backlight.value = True

display.fill(0)
display.show()

image = Image.new("1", (display.width, display.height))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", FONTSIZE)

number = 4
draw.text((0, 0), "Thomas More!", font=font, fill=255)
draw.text((0, 8), "IT Factory", font=font, fill=255)
draw.text((0, 16), "Campus Geel", font=font, fill=255)
draw.text((0, 24), "Kleinhoefstr.", font=font, fill=255)
draw.text((0, 32), str(number), font=font, fill=255)

# Display image
display.image(image)
display.show()
