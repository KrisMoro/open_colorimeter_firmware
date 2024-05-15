import board
import displayio
import busio

try:
    from fourwire import FourWire
except ImportError:
    from displayio import FourWire

from adafruit_st7789 import ST7789


def display_hut():
    #DIN = board.GP11 # MOSI pin of SPI, slave device data input
    #CLK = board.GP10 # SCK pin of SPI, clock pin
    CS = board.GP9 # Chip selection of SPI, low active
    DC = board.GP8 #Data/Command control pin (High for data; Low for command)
    RST = board.GP12 #Reset pin, low active
    BL = board.GP13 #Backlight control

    displayio.release_displays()
    spi = busio.SPI(clock=board.GP10, MOSI=board.GP11)
    while not spi.try_lock():
        pass
    spi.configure(baudrate=24000000) # Configure SPI for 24MHz
    spi.unlock()

    display_bus = FourWire(spi, command=DC, chip_select=CS, reset=RST)    
    display = ST7789(display_bus, width=240, height=240, rowstart=80, colstart=120, rotation=180)
    
    return display

