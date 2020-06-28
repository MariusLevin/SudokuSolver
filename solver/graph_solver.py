from data_structure.grid import Grid


class GraphSolver:
    def __init__(self):
        self.name = "Graph solver"
        self.__grid = Grid()

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
        return self.__grid
