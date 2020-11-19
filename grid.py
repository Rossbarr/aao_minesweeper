import numpy as np
import random

class Grid():
    def __init__(self, size = [9, 9]):
        self.grid = np.zeros(shape = size, dtype = np.int8)

    def size(self):
        return np.prod(self.grid.shape)

    def place_bombs(self, difficulty = "medium"):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if random.random() < 0.10:
                    self.grid[i, j] = -1

    def place_nums(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i, j] == -1:
                    self.add_to_adjacent_tiles([i, j])
                    
    def add_to_adjacent_tiles(self, pos):
        x, y = pos
        adjacents = [[x+1,y], [x+1,y+1], [x,y+1], [x-1,y+1], [x-1,y], [x-1,y-1], [x,y-1], [x+1,y-1]]
        for pos in adjacents:
            i, j = pos
            if 0 <= i < 9 and 0 <= j < 9 and self.grid[i, j] != -1:
                self.grid[i, j] += 1

    def render(self):
        for row in self.grid:
            for x in row:
                return


if __name__ == "__main__":
    g = Grid()
    print(g.grid)
    g.place_bombs()
    print(g.grid)
    g.place_nums()
    print(g.grid)
