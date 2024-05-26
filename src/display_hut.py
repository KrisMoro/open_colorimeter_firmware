import board
import displayio
from busio import SPI, I2C

try:
    from fourwire import FourWire
except ImportError:
    from displayio import FourWire

from adafruit_st7789 import ST7789

displayio.release_displays()

spi = SPI(clock=board.GP10, MOSI=board.GP11)
display_bus = FourWire(spi, command=board.GP8, chip_select=board.GP9, reset=board.GP12)
display = ST7789(display_bus, width=240, height=240, rowstart=80, rotation=90)

i2c = I2C(scl=board.GP1, sda=board.GP0)