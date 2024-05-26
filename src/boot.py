import board
from busio import I2C, SPI

#i2c = I2C(board.SCL, board.SDA)
spi = SPI(clock=board.GP10, MOSI=board.GP11)
