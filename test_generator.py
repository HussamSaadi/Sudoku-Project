from sudoku_generator import *
sudoku = SudokuGenerator(9, 0)
sudoku.fill_diagonal()
sudoku.fill_remaining(0, 9)
board = sudoku.get_board()
print(sudoku.get_board())
# sudoku.remove_cells()
# board = sudoku.get_board()
