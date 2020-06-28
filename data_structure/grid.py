from numpy import zeros


class Grid:
    def __init__(self):
        self.name = "Sudoku grid"
        self.matrix = zeros(shape=(9, 9))
        self.row = 9
        self.col = 9
