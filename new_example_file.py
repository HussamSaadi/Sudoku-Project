import math
import random
from cell import *
from board import *
class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0 for _ in range(row_length)] for _ in range(row_length)]
        self.box_length = int(math.sqrt(row_length))
        self.unused_in_box = {}

    def get_board(self):
        return self.board

    def test_unused_in_box(self):
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box_num = {1, 2, 3, 4, 5, 6, 7, 8, 9}
                for row in range(i, i + 3):
                    for col in range(j, j + 3):
                        if self.board[row][col] != 0:
                            box_num.remove(self.board[row][col])
                self.unused_in_box[(i, j)] = box_num

    def fill_box(self, row_start, col_start):
        box_num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(box_num_list)
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                if self.board[i][j] == 0:
                    avail_num = list(self.unused_in_box[(row_start, col_start)])
                    random.shuffle(avail_num)
                    for x_num in avail_num:
                        if x_num in box_num_list:
                            self.board[i][j] = x_num
                            box_num_list.remove(x_num)
                            break

    def fill_diagonal(self):
        self.test_unused_in_box()  # Ensure unused_in_box is initialized
        for box in range(0, 9, 3):
            self.fill_box(box, box)

    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def is_valid(self, row, col, num):
        return self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(row - row % 3,
                                                                                                 col - col % 3, num)

    def valid_in_row(self, row, num):
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        return num not in [self.board[row][col] for row in range(self.row_length)]

    def valid_in_box(self, start_row, start_col, num):
        return num not in [self.board[start_row + i][start_col + j] for i in range(3) for j in range(3)]

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    def remove_cells(self):
        count = 0
        while count != (self.removed_cells + 1):
            row = random.randint(0, 8)
            column = random.randint(0, 8)
            if self.board[row][column] != 0:
                self.board[row][column] = 0
                count += 1
def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board