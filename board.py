import pygame
import sys
from cell import *
import button
from sudoku_generator import *

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PINK = (255, 174, 201, 255)
BLUE = (0, 162, 232, 255)
LIGHT_BLUE = (173, 216, 230)
class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        # self.difficulty_number = 0
        self.selected_cell = None  # Initialize selected cell as None
        self.cells = [[Cell(0, row, col, screen) for col in range(9)] for row in range(9)]
        self.font = pygame.font.Font(None, 65)
        self.original_board = [[cell.value for cell in row] for row in self.cells]
        self.board = [[0 for _ in range(width)] for _ in range(height)]
        # self.generated_board = generate_sudoku(9, 40)
        # self.other_board = self.generated_board
        self.sudoku = SudokuGenerator(9, self.difficulty)
        self.sudoku.fill_values()
        self.solved_board = self.sudoku.get_board()
        self.sudoku.remove_cells()
        self.generated_board = self.sudoku.get_board()

        # self.generated_board = generate_sudoku(9, self.difficulty)
        self.other_generated_board = self.generated_board
        # self.generated_board = self.generate_sudoku_puzzle()
        self.user_numbers = [row[:] for row in self.generated_board]
        self.cell_value = [[0 for j in range(0, 9)] for i in range(0, 9)]

        self.board_new = []
        self.selected_cell_number = 0



    def generated_board_grab(self):
        return self.generated_board

    def draw(self):
        self.screen.fill(LIGHT_BLUE)
        for row in range(9):
            for col in range(9):
                self.cells[row][col].draw()

        # Draw grid lines
        grid_size = 720
        # grid_spacing = 80

        start_x = (self.width - grid_size) // 2
        end_x = start_x + grid_size
        start_y = (self.height - grid_size - 80) // 2
        end_y = start_y + grid_size

        pygame.draw.rect(self.screen, BLACK, pygame.Rect(start_x, start_y, grid_size, grid_size), 10)
        for i in range(1, 10):
            if i == 3 or i == 6:
                line_width = 10
            else:
                line_width = 5
            # pygame.draw.line(self.screen, BLACK, ((i * 80) + 15, 15), ((i * 80) + 15, 735), line_width)
            # pygame.draw.line(self.screen, BLACK, (15, (i * 80) + 15), (735, (i * 80) + 15), line_width)

            pygame.draw.line(self.screen, BLACK, (start_x + (i * 80), start_y), (start_x + (i * 80), start_y + grid_size),
                             line_width)
            pygame.draw.line(self.screen, BLACK, (start_x, start_y + (i * 80)), (start_x + grid_size, start_y + (i * 80)),
                             line_width)

        # load button images
        reset_img = pygame.image.load('buttonIcons/reset.png').convert_alpha()
        restart_img = pygame.image.load('buttonIcons/restart.png').convert_alpha()
        exit_img = pygame.image.load('buttonIcons/exit.png').convert_alpha()

        # create button instances
        reset_button = button.Button(153, 730, reset_img, 0.7)
        restart_button = button.Button(323, 730, restart_img, 0.7)
        exit_button = button.Button(493, 730, exit_img, 0.7)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if x >= start_x and x <= end_x and y >= start_y and y <= end_y:
                    row, col = self.click(x, y)
                    self.select(row, col)
                else:
                    if reset_button.rect.collidepoint(x, y):
                        print("Reset")

                    # Add code to handle reset button action here
                    elif restart_button.rect.collidepoint(x, y):
                        print("Restart")
                    # Add code to handle restart button action here
                    elif exit_button.rect.collidepoint(x, y):
                        print("Exit")
                        pygame.quit()
                        sys.exit()
            if event.type == pygame.KEYDOWN:
                if pygame.K_1 <= event.key <= pygame.K_9:
                    print("Number key pressed")
                    value = event.key - pygame.K_0
                    self.place_number(value)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    print("Delete key pressed")
                    self.clear()

        reset_button.draw(self.screen)
        restart_button.draw(self.screen)
        exit_button.draw(self.screen)

        pygame.display.flip()

    def draw_text(self, text, pos, font):
        text_surface = font.render(text, True, self.text_color)
        text_rect = text_surface.get_rect(center=pos)
        self.screen.blit(text_surface, text_rect)

    def click(self, x, y):
        cell_size = 720 // 9
        offset_x = 15
        offset_y = 15
        if offset_x <= x <= offset_x + 720 and offset_y <= y <= offset_y + 720:
            row = (y - offset_y) // cell_size
            col = (x - offset_x) // cell_size
            return row, col
        else:
            return None

    def clear(self):
        if self.selected_cell is not None:
            row, col = self.selected_cell
            if self.is_editable_cell(row, col):
                self.cells[row][col].set_cell_value(0)

    def is_editable_cell(self, row, col):
        return self.original_board[row][col] == 0

    def select(self, row, col):
        self.selected_cell = (row, col)
        # Update the selected attribute of the corresponding cell
        for r in range(9):
            for c in range(9):
                self.cells[r][c].selected = False  # Deselect all cells
        self.cells[row][col].selected = True
        self.selected_cell_number = self.board[row][col]

    # def sketch(self,value):
    #     if self.cells[row][col].value != 0:
    #         self.selected_cell.set_sketched_value(value)

    def place_number(self, value):
        if self.selected_cell is not None:
            row, col = self.selected_cell
            if self.cells[row][col].value == 0:
                self.cells[row][col].set_cell_value(value)
                self.board[row][col] = value

        #UPDATED BELOW VERSION TO ABOVE
        # self.selected_cell_number.set_cell_value(value)

        # if self.selected_cell is not None:
        #     row, col = self.selected_cell
        #     if self.cells[row][col].value == 0:
        #         self.cells[row][col].set_cell_value(value)
        #         self.user_numbers[row][col] = value
        #     else:
        #         self.cells[row][col].set_sketched_value(value)
        #
        # for i in self.board_new:


        # Revised this version:
        # if self.selected_cell is not None:
        #     row, col = self.selected_cell
        #     if self.cells[row][col].value == 0:
        #         self.cells[row][col].set_cell_value(value)

    def is_full(self):
        for row in range(9):
            for col in range(9):
                if self.cells[row][col].value == 0:
                    return False
        return True

    def reset_to_original(self):
        # Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit)
        for row in range(9):
            for col in range(9):
                # Check if the cell is editable (not part of the original puzzle)
                if self.is_editable_cell(row, col):
                    # Reset the cell value to its original value
                    self.board[row][col] = self.original_board[row][col]
                else:
                    # Clear the cell value
                    self.board[row][col] = 0

    # def handle_events(self):
    #     grid_size = 720
    #     # grid_spacing = 80
    #
    #     start_x = (self.width - grid_size) // 2
    #
    #
    #     start_y = (self.height - grid_size - 80) // 2
    #
    #
    #     """
    #     Handles events such as mouse clicks and keyboard input.
    #     """
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         pygame.quit()
        #         sys.exit()
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         x, y = pygame.mouse.get_pos()
        #         if x >= start_x and x <= end_x and y >= start_y and y <= end_y:
        #             row, col = self.click(x, y)
        #             self.select(row, col)
        #     if event.type == pygame.KEYDOWN:
        #         if pygame.K_1 <= event.key <= pygame.K_9:
        #             print("Number key pressed")
        #             value = event.key - pygame.K_0
        #             self.place_number(value)
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_BACKSPACE:
        #             print("Delete key pressed")
        #             self.clear()

            # Check for button clicks
            #if event.type == pygame.MOUSEBUTTONDOWN:
                #if event.button == 1:  # Left mouse button
                    # mouse_pos = pygame.mouse.get_pos()
                    #if self.reset_button_rect.collidepoint(mouse_pos):
                        #self.reset_to_original()
                    # elif self.restart_button_rect.collidepoint(mouse_pos):
                    #     self.restart_game()
                    #elif self.exit_button_rect.collidepoint(mouse_pos):
                        #sys.exit()

    def update_board(self):
        for row in range(9):
            for col in range(9):
                self.board[row][col] = self.cells[row][col].value

         # if self.generated_board[self.row][self.col] == 0:
         #     value = Cell.set_cell_value(value)
         # else:
         #     value = Cell.sketched_cell_value(value)
         #
         # for i in self.board_new:
         #     for row_no in i:
         #         for col in row_no:
         #             add.value



        #
        # self.current_answer = [[cell.value for cell in row]for row in self.board_new]
        # print(self.current_answer)
        # self.place_number()
        # for row in range(0, 9):
        #     for col in range(0, 9):  # loops through each row and col
        #         if self.other_generated_board[row][col] != 0:
        #             pass
        #         else:
        #             print(self.cells[row][col].value)
        #             self.other_generated_board[row][col].value = self.self_placed.value
        # return self.other_generated_board
        # Updates the underlying 2D board with the values in all cells.
        # for row in range(9):
        #     for col in range(9):
        #         self.board[row][col] = self.cells[row][col].value

    def get_row_values(self, row):

        return self.other_generated_board[row]

    def get_column_values(self, col):

        return self.other_generated_board[col]

    def get_grid_values(self, row_start, col_start):
        # Initialize an empty list to store the values in the 3x3 grid
        grid_values = []

        # Iterate over the cells in the 3x3 grid
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                # Append the value of the current cell to the grid_values list
                grid_values.append(self.other_generated_board[i][j])

        # Return the list of values in the 3x3 grid
        return grid_values

    def find_empty(self):
        # Finds an empty cell and returns its row and col as a tuple (row, col).
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return row, col
        return None  # Return None if no empty cell is found

    def check_board(self):
        self.update_board()
        if self.board == self.solved_board:
            return True
        else:
            return False

    # REVISED BELOW

        # self.update_board()
        # print(self.current_answer)
        # print(self.solved_board)
        # if self.current_answer == self.solved_board:
        #     return True
        # else:
        #     return False





        # self.update_board()
        # print(self.other_generated_board)
        # print(self.solved_board)
        # if self.other_generated_board == self.solved_board:
        #     return True
        # else:
        #     return False

        # REVISED THIS VERSION AGAIN
        # if not self.is_full():
        #     return False
        #
        #     # Check rows and columns for duplicates
        # for row in range(9):
        #     # Check if the values in the current row form a valid group
        #     if not self.is_valid_group(self.get_row_values(row)):
        #         return False
        #
        # for col in range(9):
        #     # Check if the values in the current column form a valid group
        #     if not self.is_valid_group(self.get_column_values(col)):
        #         return False
        #
        #     # Check 3x3 grids for duplicates
        # for row_start in range(0, 9, 3):
        #     for col_start in range(0, 9, 3):
        #         # Check if the values in the current 3x3 grid form a valid group
        #         if not self.is_valid_group(self.get_grid_values(row_start, col_start)):
        #             return False
        #
        #     # If all checks pass, return True
        # return True



        # REVISED THIS VERSION ABOVE
        # Check rows and columns for duplicates
        # for row in range(9):
        #     # Check if the values in the current row form a valid group
        #     if not self.is_valid_group(self.get_row_values(row)):
        #         return False
        #
        #     print("row")
        # for col in range(9):
        #     # Check if the values in the current column form a valid group
        #     if not self.is_valid_group(self.get_column_values(col)):
        #         return False
        #     print("col")
        #
        # # Check 3x3 grids for duplicates
        # for row_start in range(0, 9, 3):
        #     for col_start in range(0, 9, 3):
        #         # Check if the values in the current 3x3 grid form a valid group
        #         if not self.is_valid_group(self.get_grid_values(row_start, col_start)):
        #             return False
        #     print("row,col")
        # # If all checks pass, return True
        # return True

    # def check_board(self):
    #     # Check whether the Sudoku board is solved correctly.
    #     # Check rows, columns, and 3x3 grids for duplicate values
    #     for i in range(9):
    #         if not self.is_valid_group([self.board[i][j] for j in range(9)]) or not self.is_valid_group([self.board[j][i] for j in range(9)]):
    #             return False
    #     for i in range(0, 9, 3):
    #         for j in range(0, 9, 3):
    #             if not self.is_valid_group([self.board[i + m][j + n] for n in range(3) for m in range(3)]):
    #                 return False
    #     return True

    def is_valid_group(self, group):
        # Helper function to check if a group (row, column, or 3x3 grid) contains only unique values
        seen = set()
        for val in group:
            if val != 0 and val in seen:
                return False
            seen.add(val)
        return True

    # def generate_sudoku_puzzle(self):
    #     if self.difficulty == 'easy':
    #         self.difficulty_number = 30
    #         return generate_sudoku(9, self.difficulty)
    #     if self.difficulty == 'medium':
    #         self.difficulty_number = 40
    #         return generate_sudoku(9, self.difficulty)
    #     if self.difficulty == 'hard':
    #         self.difficulty_number = 50
    #         return generate_sudoku(9, self.difficulty)

    def test_rows_for_duplicates(self):
        # Test rows for duplicates
        for row in range(9):
            # Create a list of numbers for the current row with some duplicates and some unique values
            test_row = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Example row with no duplicates
            test_row_with_duplicates = [1, 2, 3, 4, 5, 6, 6, 8, 9]  # Example row with duplicates

            # Set the values of cells in the current row
            for col in range(9):
                test_row[col] = self.cells[row][col].value
                test_row_with_duplicates[col] = self.cells[row][col].value

            # Check if the is_valid_group method correctly identifies duplicates and non-duplicates
            assert self.is_valid_group(test_row) == True, f"Row {row} contains no duplicates"
            assert self.is_valid_group(test_row_with_duplicates) == False, f"Row {row} contains duplicates"

    def test_columns_for_duplicates(self):
        # Test columns for duplicates
        for col in range(9):
            # Create a list of numbers for the current column with some duplicates and some unique values
            test_col = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Example column with no duplicates
            test_col_with_duplicates = [1, 2, 3, 4, 5, 6, 6, 8, 9]  # Example column with duplicates

            # Set the values of cells in the current column
            for row in range(9):
                test_col[row] = self.cells[row][col].value
                test_col_with_duplicates[row] = self.cells[row][col].value

            # Check if the is_valid_group method correctly identifies duplicates and non-duplicates
            assert self.is_valid_group(test_col) == True, f"Column {col} contains no duplicates"
            assert self.is_valid_group(test_col_with_duplicates) == False, f"Column {col} contains duplicates"

    def test_3x3_grids_for_duplicates(self):
        # Test 3x3 grids for duplicates
        for row_start in range(0, 9, 3):
            for col_start in range(0, 9, 3):
                # Create a list of numbers for the current 3x3 grid with some duplicates and some unique values
                test_grid = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Example grid with no duplicates
                test_grid_with_duplicates = [1, 2, 3, 4, 5, 6, 6, 8, 9]  # Example grid with duplicates

                # Set the values of cells in the current 3x3 grid
                index = 0
                for i in range(3):
                    for j in range(3):
                        test_grid[index] = self.cells[row_start + i][col_start + j].value
                        test_grid_with_duplicates[index] = self.cells[row_start + i][col_start + j].value
                        index += 1

                # Check if the is_valid_group method correctly identifies duplicates and non-duplicates
                assert self.is_valid_group(
                    test_grid) == True, f"Grid at ({row_start}, {col_start}) contains no duplicates"
                assert self.is_valid_group(
                    test_grid_with_duplicates) == False, f"Grid at ({row_start}, {col_start}) contains duplicates"

# def main():
#     test_rows_for_duplicates()
#     test_columns_for_duplicates


# if __name__ == "__main__":
#     main()