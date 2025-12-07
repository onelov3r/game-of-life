from grid import Grid
from iteration import Iteration

import pygame
import time

class GameUI:

    def __init__(self, grid_size=20, cell_size=20, update_delay=0.2):
        pygame.init()

        self.grid_size = grid_size
        self.cell_size = cell_size
        self.update_delay = update_delay

        self.grid = Grid(grid_size)
        self.iteration = Iteration(self.grid)

        width = grid_size * cell_size
        height = grid_size * cell_size
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Game of Life')

        self.running = False
        self.last_update = time.time()

        self.dead_color = (0, 0, 0) 
        self.alive_color = (255, 255, 255)

    def draw_grid(self):

        self.screen.fill(self.dead_color)

        for i in range(self.grid_size):
            for j in range(self.grid_size):

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