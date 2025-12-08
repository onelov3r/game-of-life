import pygame
import Quartz
from ui import GameUI

def get_mouse_position():
    loc = Quartz.CGEventGetLocation(Quartz.CGEventCreate(None))
    return (int(loc.x), int(loc.y))

class WallpaperMode(GameUI):

    def __init__(self, cell_size=10, update_delay=0.1):
        super().__init__(cell_size=cell_size, update_delay=update_delay)
        self.mouse_pos = get_mouse_position()
        self.running = True

    def mouse_moved(self):
        pos = get_mouse_position()
        if pos != self.last_mouse_pos:
            return True
        return False
    
    def run(self):
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():

                if get_mouse_position() != self.mouse_pos or event.type == pygame.QUIT:
                    pygame.quit()
                    return

            self.update_logic()
            self.draw_grid()

            clock.tick(60)

if __name__ == "__main__":
    WallpaperMode(cell_size=10, update_delay=0.1).run()
