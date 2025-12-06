from grid import Grid
from iteration import Iteration

import time

class Game:

    def __init__(self, grid_size, grid=None):

        grid = Grid(grid_size, grid)
        print(grid)
        self.iteration = Iteration(grid)

    def start(self):

        while True:

            self.iteration.iteration()
            time.sleep(2)
