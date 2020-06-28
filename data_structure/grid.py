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

    def compare(self, grid_to_compare):
        """
        Method to compare two Grid object

        :param grid_to_compare: Grid to compare
        :return: Return the number of valid and wrong cells
        """
        result = zeros(shape=(self.row, self.col))
        cpt_true = 0
        cpt_false = 0

        for row in range(0, self.row):
            for col in range(0, self.col):
                if self.matrix[row, col] == grid_to_compare.matrix[row, col]:
                    result[row, col] = 0
                    cpt_false += 1
                else:
                    result[row, col] = 1
                    cpt_true += 1

        # print(result)

        return cpt_true, cpt_false
