import pygame
import sys

# Initialize Pygame
# will go in main function?
pygame.init()
# Set up the display
width = 750
height = 750
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sudoku Grid")

# Define colors
PINK = (255, 182, 193)
BLACK = (0, 0, 0)

class Board:
    def __init__(self, width, height, screen, difficulty):
    # Constructor for the Board class.
    # screen is a window from PyGame.
    # difficulty is a variable to indicate if the user chose easy, medium, or hard.
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

    def draw(self):
        # gives us a pink background
        screen.fill(PINK)
        # draws outside rectangle
        pygame.draw.rect(screen, BLACK, pygame.Rect(15, 15, 720, 720), 10)
        i = 1
        while (i * 80) < 720:
            if i % 3 != 0:
                line_width = 5
            else:
                line_width = 10

            # draws vertical lines
            pygame.draw.line(screen, BLACK, pygame.Vector2(((i * 80) + 15), 15), pygame.Vector2(((i * 80) + 15), 735),
                             line_width)
            # draws horizontal lines
            pygame.draw.line(screen, BLACK, pygame.Vector2(15, ((i * 80) + 15)), pygame.Vector2(735, ((i * 80) + 15)),
                             line_width)
            i += 1
            pass


    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Fill the screen with white color
            # screen.fill(PINK)

            # calls draw grid function
            self.draw()

            # Update the display
            pygame.display.flip()


    #
    # def draw(self):
    #     # Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
    #     # Draws every cell on this board.
    #     pink = (255, 182, 193)
    #     white = (255, 255, 255)
    #
    #     # Set the window dimensions
    #     WINDOW_SIZE = (500, 500)
    #     # display screen
    #
    #
    #     run = True
    #     while run:
    #         self.screen = pygame.display.set_mode(WINDOW_SIZE)
    #         pygame.display.set_caption("Sudoku Grid")
    #
    #         self.width, self.height = 9, 9
    #         CELL_SIZE = WINDOW_SIZE[0] // self.width
    #         self.screen.fill(pink)
    #
    #         for i in range(self.width + 1):
    #             line_width = 3 if i % 3 == 0 else 1
    #             pygame.draw.line(self.screen, white, (i * CELL_SIZE, 0), (i * CELL_SIZE, WINDOW_SIZE[1]), line_width)
    #             pygame.draw.line(self.screen, white, (0, i * CELL_SIZE), (WINDOW_SIZE[0], i * CELL_SIZE), line_width)
    #
    #         # Bold lines for 3x3 boxes
    #         for i in range(0, WINDOW_SIZE[0], CELL_SIZE * 3):
    #             pygame.draw.line(self.screen, white, (i, 0), (i, WINDOW_SIZE[1]), 4)
    #             pygame.draw.line(self.screen, white, (0, i), (WINDOW_SIZE[0], i), 4)
    #
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 run = False
    #                 pygame.quit()
    #                 exit(0)
    #
    #
    #     # Draw grid lines
    #     for i in range(self.width + 1):
    #         line_width = 3 if i % 3 == 0 else 1
    #         pygame.draw.line(self.screen, pink, (i * CELL_SIZE, 0), (i * CELL_SIZE, WINDOW_SIZE[1]), line_width)
    #         pygame.draw.line(self.screen, pink, (0, i * CELL_SIZE), (WINDOW_SIZE[0], i * CELL_SIZE), line_width)
    #
    #     # Bold lines for 3x3 boxes
    #     for i in range(0, WINDOW_SIZE[0], CELL_SIZE * 3):
    #         pygame.draw.line(self.screen, pink, (i, 0), (i, WINDOW_SIZE[1]), 4)
    #         pygame.draw.line(self.screen, pink, (0, i), (WINDOW_SIZE[0], i), 4)


    def select(self, row, col):
        # Marks the cell at (row, col) in the board as the current selected cell.
        # Once a cell has been selected, the user can edit its value or sketched value.
        self.selected_cell = (row, col)
        pass

    def click(self, x, y):
        #If a tuple of (x, y) coordinates is within the displayed board, this function returns a tuple of the (row, col)
        # of the cell which was clicked. Otherwise, this function returns None
        pass

    def clear(self):
        # Clears the value cell. Note that the user can only remove the cell values and sketched value that are
        # filled by themselves.
        if self.selected_cell:
            row, col = self.selected_cell
            # Check if the cell has a value filled by the user (not part of the original puzzle)
            if self.is_editable_cell(row, col):
                # Clear the value and sketch from the selected cell
                self.board[row][col] = 0  # Clear the value
                self.sketches[row][col] = None  # Clear the sketch

    def is_editable_cell(self, row, col):
        # Helper method to check if a cell is editable by the user
        return self.original_board[row][col] == 0

    def sketch(self, value):
        # Sets the sketched value of the current selected cell equal to user entered value.
        # It will be displayed at the top left corner of the cell using the draw() function.
        if self.selected_cell:
            row, col = self.selected_cell
            # Check if the cell is editable (not part of the original puzzle)
            if self.is_editable_cell(row, col):
                # Set the sketch for the selected cell
                self.sketches[row][col] = value
    pass

    def place_number(self, value):
        # Sets the value of the current selected cell equal to user entered value.
        # Called when the user presses the Enter key.
        # Sets the value of the current selected cell equal to user entered value.
        # Called when the user presses the Enter key.
        if self.selected_cell:
            row, col = self.selected_cell
            # Check if the cell is editable (not part of the original puzzle)
            if self.is_editable_cell(row, col):
                # Set the value for the selected cell
                self.board[row][col] = value
    pass

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

if __name__ == '__main__':
    # Initialize Pygame
    pygame.init()

    # Set up the display
    width = 750
    height = 750
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Sudoku Grid")

    # Create an instance of the Board class
    sudoku_board = Board(width, height, screen, difficulty="medium")
    sudoku_board.draw()
    # Main game loop
    sudoku_board.game_loop()