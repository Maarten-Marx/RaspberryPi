import adafruit_pcd8544
import board
import busio
import digitalio
from PIL import Image, ImageDraw, ImageFont


class Display:
    FONTSIZE = 10

    def __init__(self):
        spi = busio.SPI(board.SCK, MOSI=board.MOSI)
        dc = digitalio.DigitalInOut(board.D6)
        ce = digitalio.DigitalInOut(board.CE0)
        reset = digitalio.DigitalInOut(board.D5)

        self._display = adafruit_pcd8544.PCD8544(spi, dc, ce, reset)

        self._display.bias = 3
        self._display.contrast = 60

    def print_lines(self, *args: str):
        self._display.fill(0)
        self._display.show()

        image = Image.new("1", (self._display.width, self._display.height))
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", self.FONTSIZE)

        for idx, line in enumerate(args):
            draw.text((0, self.FONTSIZE * idx), line, font=font, fill=255)

        self._display.image(image)
        self._display.show()
