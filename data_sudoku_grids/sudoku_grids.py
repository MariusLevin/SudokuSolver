import numpy as np


def get_grid(difficulty):
    # Grids from: http://elmo.sbs.arizona.edu/sandiway/sudoku/examples.html
    problem = np.array([])
    solution = np.array([])
    grid_validation = True

    # Difficulty levels:
    #   - easy: 0, 1
    #   - intermediate: 2
    #   - difficult: 3, 4
    #   - very difficult: 5
    if difficulty == 0:
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
    elif difficulty == 1:
        problem = np.array([[1, 0, 0, 4, 8, 9, 0, 0, 6],
                            [7, 3, 0, 0, 0, 0, 0, 4, 0],
                            [0, 0, 0, 0, 0, 1, 2, 9, 5],
                            [0, 0, 7, 1, 2, 0, 6, 0, 0],
                            [5, 0, 0, 7, 0, 3, 0, 0, 8],
                            [0, 0, 6, 0, 9, 5, 7, 0, 0],
                            [9, 1, 4, 6, 0, 0, 0, 0, 0],
                            [0, 2, 0, 0, 0, 0, 0, 3, 7],
                            [8, 0, 0, 5, 1, 2, 0, 0, 4]])
        solution = np.array([[1, 5, 2, 4, 8, 9, 3, 7, 6],
                             [7, 3, 9, 2, 5, 6, 8, 4, 1],
                             [4, 6, 8, 3, 7, 1, 2, 9, 5],
                             [3, 8, 7, 1, 2, 4, 6, 5, 9],
                             [5, 9, 1, 7, 6, 3, 4, 2, 8],
                             [2, 4, 6, 8, 9, 5, 7, 1, 3],
                             [9, 1, 4, 6, 3, 7, 5, 8, 2],
                             [6, 2, 5, 9, 4, 8, 1, 3, 7],
                             [8, 7, 3, 5, 1, 2, 9, 6, 4]])
    else:
        print("The current difficulty isn't valid !")
        grid_validation = False

    return problem, solution, grid_validation
