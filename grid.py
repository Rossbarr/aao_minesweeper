import numpy as np
import random

class Grid():
    def __init__(self, size = [9, 9]):
        self.grid = np.zeros(shape = size, dtype = np.int8)

    def size(self):
        return np.prod(self.grid.shape)

    def place_bombs(self, num_bombs):
        for place in np.nditer(self.grid):
        return

if __name__ == "__main__":
    g = Grid()
    print(g.size())
    
