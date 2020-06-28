from data_structure.grid import Grid
import networkx as nx
#import matplotlib.pyplot as plt
import pylab


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
        self.__fill_node_colors()
        self.__init_node_available_colors()

        self.__display_graph()

        return self.__grid

    def __build_graph(self):
        """
        Method to build a graph representing the sudoku problem
        A node is like a cell, an edge a value constraint (line, column and box)
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
        Method to display a graph
        """
        nx.draw(self.__nx_graph, with_labels=True, font_weight='bold', node_size=4000)
        #plt.show()
        pylab.show()

    def __fill_node_colors(self):
        """
        Method to initialized node color
        A color represent the value taken by a node. This feature is stored as a node attribute
        """
        nx.set_node_attributes(self.__nx_graph, 0, "color")
        nx.set_node_attributes(self.__nx_graph, True, "color_upgradeable")

        for node in self.__nx_graph.nodes:
            self.__set_color(node, self.__grid.get_value(node[0], node[1]))
            if self.__get_color(node) != 0:
                self.__nx_graph.nodes[node]["color_upgradeable"] = False

    def __get_color(self, key):
        """
        Method to get the color of a node

        :param key: Name of the node
        :return: Return the color value
        """
        return self.__nx_graph.nodes[key]["color"]

    def __set_color(self, key, color):
        self.__nx_graph.nodes[key]["color"] = color

    def __is_color_upgradeable(self, key):
        """
        Method to get the upgradeable status of a node

        :param key: Name of the node
        :return: Return the upgradeable status
        """
        return self.__nx_graph.nodes[key]["color_upgradeable"]

    def __init_node_available_colors(self):
        for node in list(self.__nx_graph.nodes):
            self.__nx_graph.nodes[node]["available_colors"] = [i for i in range(1, 10)]

        for node in list(self.__nx_graph.nodes):
            node_color = self.__get_color(node)

            # Remove the node color from neighbors available colors
            for neighbor in list(self.__nx_graph.neighbors(node)):
                self.__remove_available_color(neighbor, node_color)

            if not self.__is_color_upgradeable(node):
                self.__nx_graph.nodes[node]["available_colors"] = [node_color]

    def __remove_available_color(self, key, color):
        color_buffer = self.__nx_graph.nodes[key]["available_colors"]
        if color in color_buffer:
            color_buffer.remove(color)
        self.__nx_graph.nodes[key]["available_colors"] = color_buffer

    def __add_available_color(self, key, color):
        color_buffer = self.__nx_graph.nodes[key]["available_colors"]
        if color not in color_buffer:
            color_buffer.append(color)
        self.__nx_graph.nodes[key]["available_colors"] = color_buffer
