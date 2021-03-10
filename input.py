import numpy as np
import random
from sudoku import Sudoku

def load_sudoku_csv(filename):
    grid = np.genfromtxt(filename, delimiter=",", dtype=np.int)
    return grid


def create_sudoku_by_difficult(difficult):
    assert difficult in ["easy", "medium", "hard", "evil"]
    grid = np.zeros(shape=(9, 9))
    if difficult == "easy":
        print("easy")  # 36 and more
        clues = 81 - random.sample(range(36, 40), 1)[0]
    elif difficult == "medium":
        print("medium")  # 27-36
        clues = 81 - random.sample(range(27, 36), 1)[0]
    elif difficult == "hard":
        clues = 81 - random.sample(range(19, 26), 1)[0]
        print("hard")
    else:
        clues = 81 - random.sample(range(16, 18), 1)[0]
        print("evil")

    s = Sudoku(grid)
    grid = s.solver()
    clues_indices_x = np.random.randint(0, 9, size=clues, dtype=np.int)
    clues_indices_y = np.random.randint(0, 9, size=clues, dtype=np.int)
    grid[clues_indices_x, clues_indices_y] = 0

    return grid.astype(int)


