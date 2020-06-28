from data_structure.grid import Grid


class RawForceSolver:
    def __init__(self):
        self.name = "Raw force solver"
        self.__grid = Grid()
        self.__cell_possibilities = {}

    def set_grid(self, grid_to_solve):
        """
        Method to initialize the __grid attribute with the sudoku to solve

        :param grid_to_solve: Grid containing the sudoku to solve
        """
        self.__grid = grid_to_solve

    def solve(self):
        """
        Method solving the grid

        :return: Return the solved grid
        """

        # while self.cells_to_fill.__sizeof__() != 0:
        #     print("Number of cells to fill: " + self.cells_to_fill.__sizeof__())
        #
        #     for cell in self.cells_to_fill.keys():
        #         values = [i for i in range(1, 10)]
        #
        #         row = self.grid.get_row_by_index(cell[0])
        #         col = self.grid.get_column_by_index(cell[1])
        #         box = self.grid.get_box_by_index(cell[0], cell[1])

        return self.__grid

    def fill_cell_possibilities(self):
        """
        Method to generate a list of values possible for each cell to fill
        """
        for row in range[0, self.__grid.get_number_of_row()]:
            for col in range(0, self.__grid.get_number_of_col()):
                if self.__grid.get_value(row, col) == 0:
                    self.__cell_possibilities[(row, col)] = [i for i in range(1, 10)]
