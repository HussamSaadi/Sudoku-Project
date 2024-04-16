import pygame
pygame.init()
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
        # Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
        # Draws every cell on this board.
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)

        # Set the window dimensions
        WINDOW_SIZE = (500, 500)
        screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("Sudoku Grid")
        self.width, self.height = 9, 9
        CELL_SIZE = WINDOW_SIZE[0] // self.width
        screen.fill(WHITE)
        # Draw grid lines
        for i in range(self.width + 1):
            line_width = 3 if i % 3 == 0 else 1
            pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, WINDOW_SIZE[1]), line_width)
            pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (WINDOW_SIZE[0], i * CELL_SIZE), line_width)

        # Bold lines for 3x3 boxes
        for i in range(0, WINDOW_SIZE[0], CELL_SIZE * 3):
            pygame.draw.line(screen, BLACK, (i, 0), (i, WINDOW_SIZE[1]), 4)
            pygame.draw.line(screen, BLACK, (0, i), (WINDOW_SIZE[0], i), 4)


    def select(self, row, col):
        # Marks the cell at (row, col) in the board as the current selected cell.
        # Once a cell has been selected, the user can edit its value or sketched value.
        pass

    def click(self, x, y):
        #If a tuple of (x, y) coordinates is within the displayed board, this function returns a tuple of the (row, col)
        # of the cell which was clicked. Otherwise, this function returns None
        pass

    def clear(self):
        # Clears the value cell. Note that the user can only remove the cell values and sketched value that are
        # filled by themselves.
        pass

    def sketch(self, value):
        # Sets the sketched value of the current selected cell equal to user entered value.
        # It will be displayed at the top left corner of the cell using the draw() function.
        pass

    def place_number(self, value):
        # Sets the value of the current selected cell equal to user entered value.
        # Called when the user presses the Enter key.
        pass

    def reset_to_original(self):
        # Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit)
        pass

    def is_full(self):
        # Returns a Boolean value indicating whether the board is full or not
        pass

    def update_board(self):
        # Updates the underlying 2D board with the values in all cells.
        pass

    def find_empty(self):
        # Finds an empty cell and returns its row and col as a tuple (x, y).
        pass

    def check_board(self):
        # Check whether the Sudoku board is solved correctly.
        pass