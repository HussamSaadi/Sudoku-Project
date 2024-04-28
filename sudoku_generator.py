import math, random
import copy
"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/

"""


class SudokuGenerator:
    '''
	create a sudoku board - initialize class variables and set up the 2D board
	This should initialize:
	self.row_length		- the length of each row
	self.removed_cells	- the total number of cells to be removed
	self.board			- a 2D list of ints to represent the board
	self.box_length		- the square root of row_length

	Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed

	Return:
	None
    '''

    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        # self.col_length = row_length

        # self.board = [[0 for _ in range(row_length)] for _ in range(row_length)]  #initializes the board
        self.board = [[0 for _ in range(row_length)] for _ in range(row_length)]
        self.box_length = int(math.sqrt(row_length))
        # self.unused_in_box = {}


    '''
	Returns a 2D python list of numbers which represents the board

	Parameters: None
	Return: list[list]
    '''
    def get_board(self):
        # If we are creating the board at the init method,
        # then all this should do is return the board. Hopefully :)
        # board = [['-' for _ in range(self.row_length)] for _ in range(self.row_length)]
        return self.board

    # value = '-'
    # col_list = []
    # row_list = []
    # for column in range(self.row_length - 1, -1, -1):
    #     col_list.append(value)
    #
    # for row in range(self.col_length):
    #     row_list.append(list(col_list))
    #
    # return row_list
    '''
	Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes

	Parameters: None
	Return: None
    '''

    def print_board(self):
        reversed_rows = str(self.board[::-1])
        for row_list in reversed_rows:
            new_row_list = ' '.join(row_list)
            print(int(new_row_list))




    '''
	Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True

	Parameters:
	row is the index of the row we are checking
	num is the value we are looking for in the row

	Return: boolean
    '''

    def valid_in_row(self, row, num):
        for col in range(self.row_length):
            if self.board[row][col] == num:
                return False
        return True

    '''
	Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True

	Parameters:
	col is the index of the column we are checking
	num is the value we are looking for in the column

	Return: boolean
    '''

    def valid_in_col(self, col, num):
        for row in range(self.row_length):
            if self.board[row][col] == num:
                return False
        return True

    '''
	Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
	num is the value we are looking for in the box

	Return: boolean
    '''

    def valid_in_box(self, row_start, col_start, num):
        box_numbers_list = []
        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                box_numbers_list.append(self.board[row][col])
        if num in box_numbers_list:
            return False
        else:
            return True



        # Rewrote this version:

        # for row in range(3):
        #     for col in range(3):
        #         # Check if indices are within the bounds of the board
        #         if (row_start + row) >= self.row_length or (col_start + col) >= self.row_length:
        #             return False
        #         if self.board[row_start + row][col_start + col] == num:
        #             return False
        # return True

    # def valid_in_box(self, row_start, col_start, num):
    #     for row in range(3):
    #         for col in range(3):
    #             if self.board[row_start + row][col_start + col] == num:
    #                 return False
    #     return True


    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

	Parameters:
	row and col are the row index and col index of the cell to check in the board
	num is the value to test if it is safe to enter in this cell

	Return: boolean
    '''

    def is_valid(self, row, col, num):
        initial_row = 0
        initial_col = 0
        if row == 0 or row == 1 or row == 2:
            initial_row = 0
        elif row == 3 or row == 4 or row == 5:
            initial_row = 3
        elif row == 6 or row == 7 or row == 8:
            initial_row = 6
        if col == 0 or col == 1 or col == 2:
            initial_col = 0
        elif col == 3 or col == 4 or col == 5:
            initial_col = 3
        elif col == 6 or col == 7 or col == 8:
            initial_col = 6
        if self.valid_in_row(row, num) is True and self.valid_in_col(col, num) is True and self.valid_in_box(initial_row,
                                                                                                             initial_col,
                                                                                                             num) is True:
            return True
        else:
            return False


        # Rewrote this version:

        # check_row = self.valid_in_row(row, num)
        # check_col = self.valid_in_col(col, num)
        # check_box = self.valid_in_box(row, col, num)
        # if check_row == False or check_col == False or check_box == False:
        #     return False
        # else:
        #     return True

    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

	Return: None
    '''

    # Update the fill_box method in SudokuGenerator class

    def fill_box(self, row_start, col_start):
        box_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for col in range(0, 3):
            for row in range(0, 3):
                random_numbers = random.choice(box_numbers)
                if self.valid_in_box(row_start, col_start, random_numbers) is True:
                    self.board[row_start + col][col_start + row] = random_numbers
                    box_numbers.remove(random_numbers)


        # Rewrote this version:

        # box_numbers = list(range(1, self.row_length + 1))  # List of numbers 1 to 9
        # random.shuffle(box_numbers)
        # for i in range(row_start, row_start + 3):
        #     for j in range(col_start, col_start + 3):
        #         if self.board[i][j] == 0:
        #             # Create a list of available numbers for the current cell
        #             available_numbers = [num for num in box_numbers if self.is_valid(i, j, num)]
        #             # If no available numbers, reset box_numbers and shuffle again
        #             if not available_numbers:
        #                 box_numbers = list(range(1, self.row_length + 1))
        #                 random.shuffle(box_numbers)
        #                 available_numbers = [num for num in box_numbers if self.is_valid(i, j, num)]
        #             # Shuffle the list of available numbers
        #             random.shuffle(available_numbers)
        #             if available_numbers:
        #                 self.board[i][j] = available_numbers[0]
        #                 box_numbers.remove(available_numbers[0])


    # def fill_box(self, row_start, col_start):
    #     box_numbers = list(range(1, self.row_length + 1))  # List of numbers 1 to 9
    #     random.shuffle(box_numbers)
    #     idx = 0
    #     for i in range(row_start, row_start + 3):
    #         for j in range(col_start, col_start + 3):
    #             if self.board[i][j] == 0:
    #                 # Create a list of available numbers for the current cell
    #                 available_numbers = [num for num in box_numbers if self.is_valid(i, j, num)]
    #                 # Shuffle the list of available numbers
    #                 random.shuffle(available_numbers)
    #                 if available_numbers:
    #                     self.board[i][j] = available_numbers[0]
    #                 idx += 1

    # def fill_box(self, row_start, col_start):
    #     for i in range(row_start, row_start + 3):
    #         for j in range(col_start, col_start + 3):
    #             if self.board[i][j] == 0:
    #                 # Create a list of available numbers for the current cell
    #                 available_numbers = [num for num in range(1, self.row_length + 1)
    #                                      if self.is_valid(i, j, num)]
    #                 # Shuffle the list of available numbers
    #                 random.shuffle(available_numbers)
    #                 if available_numbers:
    #                     self.board[i][j] = available_numbers[0]  # Fill the cell with the first available number

    # def fill_box(self, row_start, col_start):
    #     box_num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #     random.shuffle(box_num_list)
    #     for i in range(row_start, row_start + 3):
    #         for j in range(col_start, col_start + 3):
    #             if self.board[i][j] == 0:
    #                 avail_num = list(self.unused_in_box[(row_start, col_start)])
    #                 random.shuffle(avail_num)
    #                 for x_num in avail_num:
    #                     if x_num in box_num_list:
    #                         self.board[i][j] = x_num
    #                         box_num_list.remove(x_num)
    #                         break


    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)

	Parameters: None
	Return: None
    '''

    def fill_diagonal(self):
        # self.test_unused_in_box()
        for box in range(0, 9, 3):
            self.fill_box(box, box)

    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled

	Parameters:
	row, col specify the coordinates of the first empty (0) cell

	Return:
	boolean (whether or not we could solve the board)
    '''



    def fill_remaining(self, row, col):
        print("fill_remaining 1")
        if (col >= self.row_length and row < self.row_length - 1):
            print("fill_remaining 2")
            row += 1
            col = 0

        if row >= self.row_length and col >= self.row_length:
            print("fill_remaining 3")
            return True
        if row < self.box_length:
            print("fill_remaining 4")
            if col < self.box_length:
                print("fill_remaining 5")
                col = self.box_length
        elif row < self.row_length - self.box_length:
            print("fill_remaining 6")
            if col == int(row // self.box_length * self.box_length):
                print("fill_remaining 7")
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                print('fill_remaining 8')
                row += 1
                col = 0
                if row >= self.row_length:
                    print('fill_remaining 9')
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining

	Parameters: None
	Return: None
    '''

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called

    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

	Parameters: None
	Return: None
    '''


    def remove_cells(self):
        count = 0
        while count != (self.removed_cells):
            row = random.randint(0, 8)
            column = random.randint(0, 8)
            if self.board[row][column] != 0:
                print(f"Removing cell at row {row}, column {column}")
                self.board[row][column] = 0
            count += 1
    # def remove_cells(self):
    #     count = 0
    #     while count != (self.removed_cells + 1):
    #         row = random.randint(0, 8)
    #         column = random.randint(0, 8)
    #         if self.board[row][column] != 0:
    #             self.board[row][column] = 0
    #             count += 1


    '''
    DO NOT CHANGE
    Provided for students
    Given a number of rows and number of cells to remove, this function:
    1. creates a SudokuGenerator
    2. fills its values and saves this as the solved state
    3. removes the appropriate number of cells
    4. returns the representative 2D Python Lists of the board and solution

    Parameters:
    size is the number of rows/columns of the board (9 for this project)
    removed is the number of cells to clear (set to 0)

    Return: list[list] (a 2D Python list to represent the board)
    '''

def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    solution = copy.deepcopy(sudoku.get_board())
    # deep copy of sol

    sudoku.remove_cells()
    board = sudoku.get_board()
    return board, solution




# Testing:

def test_methods():
    # Initialize SudokuGenerator
    sudoku = SudokuGenerator(9, 0)
    sudoku.board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    # Test valid_in_row
    assert sudoku.valid_in_row(0, 5) == False
    assert sudoku.valid_in_row(0, 6) == True

    # Test valid_in_col
    assert sudoku.valid_in_col(0, 5) == False
    assert sudoku.valid_in_col(0, 2) == True

    # Test valid_in_box
    assert sudoku.valid_in_box(0, 0, 5) == False
    assert sudoku.valid_in_box(0, 0, 2) == True

    # Test is_valid
    assert sudoku.is_valid(0, 0, 5) == False
    assert sudoku.is_valid(0, 0, 2) == True

    print("All tests passed!")

test_methods()



