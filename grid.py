class Grid:

    def __init__(self, grid_width=8, grid_height=8, init_grid=None):
        self.grid_width = grid_width
        self.grid_height = grid_height
        if init_grid is None:
            import random
            self.grid = [[random.randint(0, 1) for _ in range(self.grid_width)] for _ in range(self.grid_height)]
        else:
            if len(init_grid) != grid_height:
                raise ValueError('Grid size is not equal to \'grid_size\'')
            self.grid = init_grid

    def get(self, i, j):
        i %= self.grid_height
        j %= self.grid_width
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
        return Grid(self.grid_width, self.grid_height, grid_copy)

    def __repr__(self):
        string = 'Grid:\n'
        for row in self.grid:
            string += str(row)
            string += '\n'
        return string