from sudoku import Sudoku
import numpy as np
from input import load_sudoku_csv


"""
grid = np.asarray([[3, 0, 6, 5, 0, 8, 4, 0, 0],
                                [5, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 1],
                                [0, 0, 3, 0, 1, 0, 0, 8, 0],
                                [9, 0, 0, 8, 6, 3, 0, 0, 5],
                                [0, 5, 0, 0, 9, 0, 6, 0, 0],
                                [1, 3, 0, 0, 0, 0, 2, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 7, 4],
                                [0, 0, 5, 2, 0, 6, 3, 0, 0]])
"""
grid = load_sudoku_csv("sudoku.csv")
s = Sudoku(grid)
print("Sudoku Input")
s.show_grid()
print()
print("Sudoku Solution")
print(s.solver())