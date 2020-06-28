from data_structure.grid import Grid
import networkx as nx
import matplotlib.pyplot as plt


class GraphSolver:
    def __init__(self):
        self.name = "Graph solver"
        self.__grid = Grid()
        self.__nx_graph = nx.Graph()

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
        self.__build_graph()

        self.__display_graph()

        return self.__grid

    def __build_graph(self):
        """

        :return:
        """
        # Create nodes
        for row in range(0, self.__grid.get_number_of_row()):
            for col in range(0, self.__grid.get_number_of_col()):
                self.__nx_graph.add_node((row, col))

        # Create edges
        for current_node in list(self.__nx_graph.nodes):
            for other_node in list(self.__nx_graph.nodes):
                # Do not apply edge treatment on node if it is itself
                if current_node == other_node:
                    continue

                # Create an edge if nodes are in the same line or column
                if current_node[0] == other_node[0] or \
                        current_node[1] == other_node[1]:
                    self.__nx_graph.add_edge(current_node, other_node)

                box_index1 = self.__grid.get_box_index(current_node[0], current_node[1])
                box_index2 = self.__grid.get_box_index(other_node[0], other_node[1])

                # Create an edge if nodes are in the same box
                if box_index1 == box_index2:
                    self.__nx_graph.add_edge(current_node, other_node)

    def __display_graph(self):
        """

        """
        nx.draw(self.__nx_graph, with_labels=True, font_weight='bold')
        plt.show()
