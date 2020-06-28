from numpy import zeros


class Grid:
    def __init__(self):
        self.name = "Sudoku grid"
        self.matrix = zeros(shape=(9, 9))
        self.row = 9
        self.col = 9

    def set_grid(self, sudoku_array):
        """
        Method to load a sudoku grid in the Grid class

        :param sudoku_array: numpy array containing the sudoku grid
        """
        self.matrix = sudoku_array
        self.row, self.col = self.matrix.shape