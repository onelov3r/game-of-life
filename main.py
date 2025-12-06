from grid import Grid
from iteration import Iteration

init_grid = [
    [1, 0, 0, 0, 1],
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1]
]

grid = Grid(len(init_grid), init_grid)
iteration = Iteration(grid)

print(grid)
for i in range(10):
    iteration.iteration()