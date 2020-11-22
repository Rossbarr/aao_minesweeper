from grid import Grid

class Game():
    def __init__(self):
        self.grid = Grid()

    def run(self):
        print("hello?")
        while not self.grid.solved():
            self.grid.render()
            pos = input("Enter a position (e.g. '4 5'): ")
            pos = self.parse_pos(pos)
            val = input("Enter a command (flag - 'F', click - 'C'): ")
            val = self.parse_val(val)
            successful = self.grid.execute(pos, val)
            print(successful)
            if not successful:
                print("You lose!")
                return

    def parse_pos(self, pos):
        arr = []
        num = ''
        for char in pos:
            if char == ' ':
                arr.append(int(num))
                num = ''
            else:
                num = num + char
        arr.append(int(num))

        if len(arr) is not 2 or type(arr) is not list:
            raise Exception("I'm sorry; I couldn't read that. Please try again.")
        return arr

    def parse_val(self, val):
        return val

if __name__ == "__main__":
    g = Game()
    g.run()
