import adafruit_pcd8544
import board
import busio
import digitalio
from PIL import Image, ImageDraw, ImageFont


# Class for controlling the display
class Display:
    FONTSIZE = 10

    def __init__(self):
        # Define the right pins
        spi = busio.SPI(board.SCK, MOSI=board.MOSI)
        dc = digitalio.DigitalInOut(board.D6)
        ce = digitalio.DigitalInOut(board.CE0)
        reset = digitalio.DigitalInOut(board.D5)

        # Create the object to interact with the display
        self._display = adafruit_pcd8544.PCD8544(spi, dc, ce, reset)

        # I found this combination of options to be the most readable
        self._display.bias = 3
        self._display.contrast = 60

    def print_lines(self, *args: str):
        # Clear the monitor
        self._display.fill(0)
        self._display.show()

        # Create a new image with type 1, and the appropriate width and height
        image = Image.new("1", (self._display.width, self._display.height))
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", self.FONTSIZE)

        # Write all lines, offset downwards each line
        for idx, line in enumerate(args):
            draw.text((0, self.FONTSIZE * idx), line, font=font, fill=255)

        # Show the result
        self._display.image(image)
        self._display.show()
