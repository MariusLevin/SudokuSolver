import numpy as np
from math import floor


class Grid:
    def __init__(self):
        self.name = "Sudoku grid"
        self.__matrix = np.zeros(shape=(9, 9))
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
        result = np.zeros(shape=(self.__number_of_row, self.__number_of_col))
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

    def get_grid_size(self):
        """
        Method to get the grid size

        :return: Return the number of row and column
        """
        return self.__number_of_row, self.__number_of_col

    def get_number_of_row(self):
        """
        Method ti get the number of row

        :return: Return the number of row
        """
        return self.__number_of_row

    def get_number_of_col(self):
        """
        Method to get the number of column

        :return: Return the number of column
        """
        return self.__number_of_col

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

    def get_box_by_index(self, row, col):
        """
        Method to get a complete box of the grid

        :param row: Rox index of a cell in the needed box
        :param col: Column index of a cell in the needed box
        :return: Return the box as an array of values
        """
        return self.get_box(self.get_box_index(row, col))

    def get_box_index(self, row, col):
        """
        Method to get the box index of a selected cell

        :param row: Row index of the selected cell
        :param col: Column index of the selected cell
        :return: Return the box index
        """
        return floor(row / 3) * 3 + floor(col / 3)

    def get_box(self, index):
        """
        Method to get the box from its index

        :param index: Index of the needed box
        :return: Return the box as an array of values
        """
        index_min_row = floor(index / 3) * 3
        index_max_row = (floor(index / 3) + 1) * 3
        index_min_col = (index % 3) * 3
        index_max_col = ((index % 3) + 1) * 3
        box = self.matrix[index_min_row:index_max_row, index_min_col:index_max_col]

        return box

    def get_value(self, row_index, col_index):
        """
        Method to get the value of o selected cell

        :param row_index: Row index of the selected cell
        :param col_index: Column index of the selected cell
        :return: Return the value of the cell
        """
        return self.matrix[row_index, col_index]
