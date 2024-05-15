import board
import displayio
import constants
import display_hut


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
        display_hut.display_hut().root_group=self.group
        display_hut.display_hut().show()