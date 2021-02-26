import numpy as np
import random


def load_sudoku_csv(filename):
    grid = np.genfromtxt(filename, delimiter=",", dtype=np.int)
    return grid


def create_sudoku_by_difficult(difficult):
    assert difficult in ["easy", "medium", "hard", "evil"]
    grid = np.zeros(shape=(9, 9))
    if difficult == "easy":
        print("easy")  # 36 and more
        clues = 36
    elif difficult == "medium":
        print("medium")  # 27-36
        clues = 27  #
    elif difficult == "hard":
        clues = 27  # 19-26
        print("hard")
    else:
        clues = 18  # 0-18
        print("evil")
        clues = 1

    clues_number = random.sample(range(1, 10), population=clues)
    clues_indices_x = random.sample(range(1, 10), population=clues)
    clues_indices_y = random.sample(range(1, 10), population=clues)
    # TODO inserire i numeri in grid

    return grid
