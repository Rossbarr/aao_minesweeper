from tile import Tile
import numpy as np
import random

class Grid():
    def __init__(self, size = [9, 9]):
        self.fill_grid(size)
        self.place_bombs()
        self.place_nums()

    def size(self):
        return np.prod(self.grid.shape)

    def fill_grid(self, size):
        self.grid = np.empty(size, dtype = type(Tile))
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                self.grid[i,j] = Tile() #revealed = True)

    def place_bombs(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if random.random() < 0.10:
                    self.grid[i, j].value = -1

    def place_nums(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i, j].value == -1:
                    self.add_to_adjacent_tiles([i, j])
                    
    def add_to_adjacent_tiles(self, pos):
        x, y = pos
        adjacents = [[x+1,y], [x+1,y+1], [x,y+1], [x-1,y+1], [x-1,y], [x-1,y-1], [x,y-1], [x+1,y-1]]
        for pos in adjacents:
            i, j = pos
            if 0 <= i < 9 and 0 <= j < 9 and self.grid[i, j].value != -1:
                self.grid[i, j].value += 1

    def render(self):
        print("   ", end = "")
        for j in range(len(self.grid[0])):
             print(j, end = " ")
        
        print("\n------------------------")
        for i in range(len(self.grid)):
            print("{}| ".format(i), end = "")
            for j in range(len(self.grid[0])):
                if self.grid[i, j].revealed:
                    print("{} ".format(self.grid[i, j].value), end = "")
                else:
                    print("  ", end = "")
            print("\n")

if __name__ == "__main__":
    g = Grid()
    g.render()
