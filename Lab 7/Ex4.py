import board
import busio
import digitalio
from PIL import Image, ImageOps
import adafruit_pcd8544

spi = busio.SPI(board.SCK, MOSI=board.MOSI)
dc = digitalio.DigitalInOut(board.D6)
cs = digitalio.DigitalInOut(board.CE1)
reset = digitalio.DigitalInOut(board.D5)

display = adafruit_pcd8544.PCD8544(spi, dc, cs, reset)

display.bias = 4
display.contrast = 60

display.fill(0)
display.show()

with Image.open("me.jpg") as img:
    img = img.resize((display.width, display.height), Image.ANTIALIAS)
    inv = ImageOps.invert(img).convert("1")
    display.image(inv)
    display.show()
