import pygame
import sys
from cell import *
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
        self.selected_cell = None  # Initialize selected cell as None
        self.cells = [[Cell(0, row, col, screen) for col in range(9)] for row in range(9)]
        self.font = pygame.font.Font(None, 65)
        self.original_board = [[cell.value for cell in row] for row in self.cells]
        self.board = [[0 for _ in range(width)] for _ in range(height)]

    def draw(self):
        self.screen.fill(LIGHT_BLUE)
        for row in range(9):
            for col in range(9):
                self.cells[row][col].draw()

        pygame.draw.rect(self.screen, BLACK, pygame.Rect(15, 15, 720, 720), 10)
        for i in range(1, 10):

            if i == 3 or i == 6:
                line_width = 10
            else:
                line_width = 5
            pygame.draw.line(self.screen, BLACK, ((i * 80) + 15, 15), ((i * 80) + 15, 735), line_width)
            pygame.draw.line(self.screen, BLACK, (15, (i * 80) + 15), (735, (i * 80) + 15), line_width)
        pygame.display.flip()

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

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row, col = self.click(x, y)
                self.select(row, col)
            if event.type == pygame.KEYDOWN:
                if pygame.K_1 <= event.key <= pygame.K_9:
                    value = event.key - pygame.K_0
                    self.place_number(value)
                elif event.key == pygame.K_BACKSPACE:
                    self.clear()

    def place_number(self, value):
        if self.selected_cell is not None:
            row, col = self.selected_cell
            if self.cells[row][col].value == 0:
                self.cells[row][col].set_cell_value(value)

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

    def handle_events(self):
        """
        Handles events such as mouse clicks and keyboard input.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row, col = self.click(x, y)
                self.select(row, col)
            if event.type == pygame.KEYDOWN:
                if pygame.K_1 <= event.key <= pygame.K_9:
                    print("Number key pressed")
                    value = event.key - pygame.K_0
                    self.place_number(value)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    print("Delete key pressed")
                    self.clear()



    def is_full(self):
        # Returns a Boolean value indicating whether the board is full or not
        for row in range(9):
            for col in range(9):
                # If any cell is empty, return False
                if self.board[row][col] == 0:
                    return False
        # If no empty cells are found, return True
        return True

    def update_board(self):
        # Updates the underlying 2D board with the values in all cells.
        for row in range(9):
            for col in range(9):
                self.board[row][col] = self.cells[row][col].value

    def find_empty(self):
        # Finds an empty cell and returns its row and col as a tuple (row, col).
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return row, col
        return None  # Return None if no empty cell is found

    def check_board(self):
        # Check whether the Sudoku board is solved correctly.
        # Check rows, columns, and 3x3 grids for duplicate values
        for i in range(9):
            if not self.is_valid_group([self.board[i][j] for j in range(9)]) or \
                    not self.is_valid_group([self.board[j][i] for j in range(9)]):
                return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not self.is_valid_group([self.board[i + m][j + n] for n in range(3) for m in range(3)]):
                    return False
        return True

    def is_valid_group(self, group):
        # Helper function to check if a group (row, column, or 3x3 grid) contains only unique values
        seen = set()
        for val in group:
            if val != 0 and val in seen:
                return False
            seen.add(val)
        return True