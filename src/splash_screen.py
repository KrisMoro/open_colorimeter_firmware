import board
import displayio
import constants_2591

class SplashScreen:

    def __init__(self):
        filename = f'{constants_2591.SPLASHSCREEN_BMP}'
        self.bitmap = displayio.OnDiskBitmap(filename)
        self.tile_grid = displayio.TileGrid(
                self.bitmap, 
                pixel_shader = self.bitmap.pixel_shader, 
                )
        self.group = displayio.Group()
        self.group.append(self.tile_grid)

    def show(self):
        board.DISPLAY.root_group = self.group
