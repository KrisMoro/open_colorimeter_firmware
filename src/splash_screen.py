import board
import displayio
import constants
from display_hut import display
class SplashScreen:

    def __init__(self):
        filename = f'{constants.SPLASHSCREEN_BMP}'
        self.bitmap = displayio.OnDiskBitmap(filename)
        self.tile_grid = displayio.TileGrid(
                self.bitmap, 
                pixel_shader = self.bitmap.pixel_shader, 
                )
        self.group = displayio.Group()
        self.group.append(self.tile_grid)

    def show(self):
        display.root_group=self.group
    