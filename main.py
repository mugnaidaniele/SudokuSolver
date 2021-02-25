from sudoku import Sudoku

s = Sudoku()
print("Sudoku Input")
s.show_grid()
print()
print("Sudoku Solution")
print(s.solver())