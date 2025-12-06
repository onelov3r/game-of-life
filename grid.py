class Grid:

    def __init__(self, grid_size=8, init_grid=None):
        self.grid_size = grid_size
        if init_grid is None:
            self.grid = [([0] * grid_size)] * grid_size
        else:
            if len(init_grid) != grid_size:
                raise ValueError('Grid size is not equal to \'grid_size\'')
            self.grid = init_grid

    def get(self, i, j):
        if i < 0 or i > self.grid_size - 1:
            return 0
        if j < 0 or j > self.grid_size - 1:
            return 0
        return self.grid[i][j]
    
    def set(self, i, j, value):
        if value not in (0, 1):
            raise ValueError('value should be 0 (dead) or 1 (alive)')
        if isinstance(value, int):
            self.grid[i][j] = value
        else:
            raise ValueError(f'value should be an integer, got {type(value).__name__}')

    def clone(self):
        import copy
        grid_copy = [row.copy() for row in self.grid]
        return Grid(self.grid_size, grid_copy)

    def __repr__(self):
        string = 'Grid:\n'
        for row in self.grid:
            string += str(row)
            string += '\n'
        return string