from numpy import zeros


class Grid:
    def __init__(self):
        self.name = "Sudoku grid"
        self.__matrix = zeros(shape=(9, 9))
        self.__number_of_row = 9
        self.__number_of_col = 9

    def set_grid(self, sudoku_array):
        """
        Method to load a sudoku grid in the Grid class

        :param sudoku_array: numpy array containing the sudoku grid
        """
        self.__matrix = sudoku_array
        self.__number_of_row, self.__number_of_col = self.__matrix.shape

    def compare(self, grid_to_compare):
        """
        Method to compare two Grid object

        :param grid_to_compare: Grid to compare
        :return: Return the number of valid and wrong cells
        """
        result = zeros(shape=(self.__number_of_row, self.__number_of_col))
        cpt_true = 0
        cpt_false = 0

        for row in range(0, self.__number_of_row):
            for col in range(0, self.__number_of_col):
                if self.__matrix[row, col] == grid_to_compare.__matrix[row, col]:
                    result[row, col] = 0
                    cpt_false += 1
                else:
                    result[row, col] = 1
                    cpt_true += 1

        # print(result)

        return cpt_true, cpt_false

    def get_row_by_index(self, index):
        """
        Method to get a complete row of the grid

        :param index: Index of the needed row
        :return: Return the row as a list of values
        """
        return self.__matrix[index, :]

    def get_column_by_index(self, index):
        """
        Method to get a complete column of the grid

        :param index: Index of the needed column
        :return: return the column as a list of values
        """
        return self.__matrix[:, index]
