from data_sudoku_grids.sudoku_grids import get_grid
from data_structure.grid import Grid
from solver.raw_force_solver import RawForceSolver
from solver.graph_solver import GraphSolver

if __name__ == '__main__':
    # Parameters
    SOLVER_TYPE = "RAW"  # "RAW" or "GRAPH"

    problem, solution, grid_validation = get_grid(difficulty=0)

    # Sanity check
    if not grid_validation:
        print("Failed to load the grid problem !")
        exit(1)

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