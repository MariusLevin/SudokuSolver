import numpy as np
from data_structure.grid import Grid
from solver.raw_force_solver import RawForceSolver
from solver.graph_solver import GraphSolver

if __name__ == '__main__':
    # Parameters
    SOLVER_TYPE = "RAW"  # "RAW" or "GRAPH"

    problem = np.array([[0, 0, 0, 2, 6, 0, 7, 0, 1],
                        [6, 8, 0, 0, 7, 0, 0, 9, 0],
                        [1, 9, 0, 0, 0, 4, 5, 0, 0],
                        [8, 2, 0, 1, 0, 0, 0, 4, 0],
                        [0, 0, 4, 6, 0, 2, 9, 0, 0],
                        [0, 5, 0, 0, 0, 3, 0, 2, 8],
                        [0, 0, 9, 3, 0, 0, 0, 7, 4],
                        [0, 4, 0, 0, 5, 0, 0, 3, 6],
                        [7, 0, 3, 0, 1, 8, 0, 0, 0]])

    solution = np.array([[4, 3, 5, 2, 6, 9, 7, 8, 1],
                         [6, 8, 2, 5, 7, 1, 4, 9, 3],
                         [1, 9, 7, 8, 3, 4, 5, 6, 2],
                         [8, 2, 6, 1, 9, 5, 3, 4, 7],
                         [3, 7, 4, 6, 8, 2, 9, 1, 5],
                         [9, 5, 1, 7, 4, 3, 6, 2, 8],
                         [5, 1, 9, 3, 2, 6, 8, 7, 4],
                         [2, 4, 8, 9, 5, 7, 1, 3, 6],
                         [7, 6, 3, 4, 1, 8, 2, 5, 9]])

    gridProblem = Grid()
    gridProblem.set_grid(problem)

    gridAnswer = Grid()

    if SOLVER_TYPE == "RAW":
        solver = RawForceSolver()
        solver.set_grid(gridProblem)

        gridAnswer = solver.solve()

    elif SOLVER_TYPE == "GRAPH":
        solver = GraphSolver()
        solver.set_grid(gridProblem)

        gridAnswer = solver.solve()

    gridSolution = Grid()
    gridSolution.set_grid(solution)

    valid, error = gridSolution.compare(gridAnswer)

    print("Number of valid cells: " + str(valid))
    print("Number of error cells: " + str(error))