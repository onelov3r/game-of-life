from grid import Grid

class Iteration:

    def __init__(self, grid):

        if isinstance(grid, Grid):
            self.grid = grid
        else:
            raise ValueError('\'grid\' shoulde be an instance of class Grid')
    
    def _count_neighbors(grid, i, j):
        neighbors_count = 0
        neighbors_count += grid.get(i - 1, j)
        neighbors_count += grid.get(i - 1, j - 1)
        neighbors_count += grid.get(i - 1, j + 1)
        neighbors_count += grid.get(i, j - 1)
        neighbors_count += grid.get(i, j + 1)
        neighbors_count += grid.get(i + 1, j)
        neighbors_count += grid.get(i + 1, j - 1)
        neighbors_count += grid.get(i + 1, j + 1)
        return neighbors_count

    def iteration(self):
        
        new_grid = self.grid.clone()
        for i, row in enumerate(self.grid.grid):
            for j, cell in enumerate(row):
                neighbors = self._count_neighbors(self.grid, i, j)
                if cell == 0 and neighbors == 3:
                    new_grid.set(i, j, 1)
                elif cell == 1 and neighbors not in (2, 3):
                    new_grid.set(i, j, 0)
        self.grid = new_grid
        print(self.grid)