class Tile():
    def __init__(self, value = 0, revealed = True):
        """
        The only two variables necessary are revealed and value:
        
        Revealed tells the board if the user should be able to see the value.
        
        Value does 2 things:
            If value is -1, then the tile is a bomb.
                If revealed becomes true, then the bomb explodes. Game over.
            If the value is not -1, then the value indicates how many adjacent tiles are bombs.
        """
        self.value = value
        self.revealed = revealed

    def reveal(self):
        self.revealed = True
        if value == -1:
            return False
        else:
            return True
