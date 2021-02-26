import numpy as np
import time


class Sudoku:

    def __init__(self, grid):
        self.grid = grid

    def is_solved(self):
        solved = True
        for i in range(0, len(self.grid)):
            row = self.grid[i][:]
            for element in row:
                if element == 0:
                    solved = False
                    break
        return solved

    def is_used_in_row(self, row, target):
        for i in range(0, len(self.grid)):
            if self.grid[row][i] == target:
                return True
        return False

    def is_used_in_column(self, column, target):
        for i in range(0, len(self.grid)):
            if self.grid[i][column] == target:
                return True
        return False

    def get_subgrid(self, i, j):
        row = i // 3 * 3
        column = j // 3 * 3
        return self.grid[row:row + 3, column: column + 3]

    def is_used_in_subgrid(self, i, j, target):
        sb = self.get_subgrid(i, j)
        for k in range(0, 3):
            for l in range(0, 3):
                if sb[k][l] == target:
                    return True
        return False

    def is_safe(self, x, y, target):
        if self.is_used_in_row(x, target) or self.is_used_in_column(y, target) or self.is_used_in_subgrid(x, y, target):
            return False
        return True

    def show_grid(self):
        print(self.grid)

    def show_subgrid(self, i, j):
        print(self.get_subgrid(i, j))

    def solve(self):
        row, col = 0, 0
        to_fill = False

        for row in range(0, len(self.grid)):
            for col in range(0, len(self.grid[0])):
                if self.grid[row][col] == 0:
                    to_fill = True  # Cella Vuota
                    break
            if to_fill:  # Interrompo double for, (col,row) indicano la cella selezionata
                break

        if not to_fill:  # No Cella Vuota -> terminato
            return True
        for num in range(1, 10):  # Cerco numero per la cella
            if self.is_safe(row, col, num):
                self.grid[row][col] = num
                if self.solve():  # provo a risolvere nuovo sudoku aggiornato
                    return True
                self.grid[row][col] = 0  # se non riesco a risolverlo riassegno la cella vuota
        return False

    def solver(self):
        if self.solve():
            return self.grid
        return "No Sol"
