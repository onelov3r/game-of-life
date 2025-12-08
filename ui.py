from grid import Grid
from iteration import Iteration

import pygame
import time

class GameUI:

    def __init__(self, cell_size=20, update_delay=0.2):
        pygame.init()

        self.cell_size = cell_size

        info = pygame.display.Info()
        screen_w, screen_h = info.current_w, info.current_h

        self.grid_width = screen_w // cell_size
        self.grid_height = screen_h // cell_size

        self.update_delay = update_delay

        self.grid = Grid(self.grid_width, self.grid_height)
        self.iteration = Iteration(self.grid)

        self.window_width = self.cell_size * self.grid_width
        self.window_height = self.cell_size * self.grid_height

        self.screen = pygame.display.set_mode((self.window_width, self.window_height), pygame.NOFRAME | pygame.FULLSCREEN)
        pygame.display.set_caption('Game of Life')

        self.running = False
        self.last_update = time.time()

        self.dead_color = (0x00, 0x1a, 0x00)
        self.alive_color = (0x00, 0xFF, 0x41)

    def draw_grid(self):

        self.screen.fill(self.dead_color)

        for i in range(self.grid_height):
            for j in range(self.grid_width):

                value = self.grid.get(i, j)

                color = self.alive_color if value == 1 else self.dead_color

                rect = pygame.Rect(
                    j * self.cell_size,
                    i * self.cell_size, 
                    self.cell_size,
                    self.cell_size
                )
                pygame.draw.rect(self.screen, color, rect)
                #pygame.draw.rect(self.screen, (200, 200, 200), rect, 1)

        pygame.display.flip()

    def handle_mouse(self):
        
        x, y = pygame.mouse.get_pos()
        j = x // self.cell_size
        i = y // self.cell_size

        if not self.running:
            current = self.grid.get(i, j)
            new_value = 1 - current
            self.grid.set(i, j, new_value)

    def update_logic(self):

        now = time.time()
        if self.running and now - self.last_update >= self.update_delay:

            new_grid = self.iteration.iteration()
            self.grid = new_grid
            self.iteration.grid = new_grid
            self.last_update = now

    def run(self):

        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_mouse()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.running = not self.running

            self.update_logic()
            self.draw_grid()

            clock.tick(60)