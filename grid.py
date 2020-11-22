from tile import Tile
import numpy as np
import random

class Grid():
    def __init__(self, size = [9, 9]):
        self.fill_grid(size)
        self.place_bombs()
        self.place_nums()
        self.clicked = []

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
                elif self.grid[i, j].flagged == True:
                    print("F ", end = "")
                else:
                    print("  ", end = "")
            print("")
        
    def execute(self, pos, val):
        if val is 'F' or val is 'f':
            return self.flag(pos)
        elif val is 'C' or val is 'c':
            return self.click(pos)


    def flag(self, pos):
        x, y = pos
        return self.grid[x, y].flag()

    def click(self, pos):
        x, y = pos
        successful = self.grid[x, y].reveal()
        if successful is 0: #indicates a tile with no bombs surrounding it.
            self.click_adjacents(pos)
            return True
        elif successful is -1: #indicates a bomb
            return False
        else:
            self.clicked.append([x, y])
            return True

    def click_adjacents(self, pos):
        x, y = pos
        self.clicked.append([x, y])
        adjacents = [[x+1,y], [x+1,y+1], [x,y+1], [x-1,y+1], [x-1,y], [x-1,y-1], [x,y-1], [x+1,y-1]]
        for adj_pos in adjacents:
            i, j = adj_pos
            if 0 <= i < 9 and 0 <= j < 9 and [i, j] not in self.clicked:
                self.click([i, j])


    def solved(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i, j].value == -1 and self.grid[i, j].flagged == False:
                    return False
        return True

if __name__ == "__main__":
    g = Grid()
    g.render()
