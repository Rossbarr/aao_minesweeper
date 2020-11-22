class Tile():
    def __init__(self, value = 0):
        self.value = value
        self.revealed = False
        self.flagged = False

    def reveal(self):
        self.revealed = True
        return self.value

    def flag(self):
        self.flagged = not self.flagged
        return True
