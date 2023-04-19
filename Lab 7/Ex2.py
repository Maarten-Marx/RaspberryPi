import board
import busio
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_pcd8544
import adafruit_mcp3xxx.mcp3008
from adafruit_mcp3xxx.analog_in import AnalogIn
import time

spi = busio.SPI(board.SCK, MOSI=board.MOSI)
dc = digitalio.DigitalInOut(board.D6)
cs = digitalio.DigitalInOut(board.CE1)
reset = digitalio.DigitalInOut(board.D5)

potentiometer_spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
potentiometer_cs = digitalio.DigitalInOut(board.CE0)

mcp = adafruit_mcp3xxx.mcp3008.MCP3008(potentiometer_spi, potentiometer_cs)
mcp_channel_0 = AnalogIn(mcp, adafruit_mcp3xxx.mcp3008.P0)
mcp_channel_1 = AnalogIn(mcp, adafruit_mcp3xxx.mcp3008.P1)

display = adafruit_pcd8544.PCD8544(spi, dc, cs, reset)

FONTSIZE = 10

display.bias = 5
display.contrast = 50

image = Image.new("1", (display.width, display.height))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", FONTSIZE)

while True:
    draw.rectangle((0, 0, display.width, display.height), outline=0, fill=0)

    potentiometer_value_0 = mcp_channel_0.value
    potentiometer_value_1 = mcp_channel_1.value
    draw.text((0, 0), "ADC value", font=font, fill=255)
    draw.text((0, 10), "on display", font=font, fill=255)
    draw.text((0, 20), "in0=" + str(potentiometer_value_0), font=font, fill=255)
    draw.text((0, 30), "in1=" + str(potentiometer_value_1), font=font, fill=255)

    display.fill(0)
    display.show()

    display.image(image)
    display.show()

    time.sleep(1)
