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
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.selected_cell = None  # Initialize selected cell as None
        self.board = [[0] * 9 for _ in range(9)]
        self.font = pygame.font.Font(None, 65)

    def draw(self):
        """
        Draws the Sudoku grid on the screen.
        """
        PINK = (255, 182, 193)
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)

        self.screen.fill(PINK)
        pygame.draw.rect(self.screen, BLACK, pygame.Rect(15, 15, 720, 720), 10)
        for i in range(1, 10):
            line_width = 5 if i % 3 != 0 else 10
            pygame.draw.line(self.screen, BLACK, ((i * 80) + 15, 15), ((i * 80) + 15, 735), line_width)
            pygame.draw.line(self.screen, BLACK, (15, (i * 80) + 15), (735, (i * 80) + 15), line_width)

        # Fill selected cell with white color if it's selected
        if self.selected_cell is not None:
            row, col = self.selected_cell
            cell_size = 720 // 9
            offset_x = 15
            offset_y = 15
            pygame.draw.rect(self.screen, WHITE, ((col * cell_size) + offset_x, (row * cell_size) + offset_y, cell_size, cell_size))
        self.draw_numbers()

    def draw_numbers(self):
        """
        Draws the numbers in cells.
        """
        for row in range(9):
            for col in range(9):
                value = self.board[row][col]
                if value != 0:
                    text_surface = self.font.render(str(value), True, BLACK)
                    cell_rect = pygame.Rect(col * 80 + 20, row * 80 + 20, 80, 80)
                    text_rect = text_surface.get_rect(center=cell_rect.center)
                    self.screen.blit(text_surface, text_rect)

    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Fill the screen with white color
            # screen.fill(PINK)
            self.handle_events()
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
        cell_size = 720 // 9
        offset_x = 15
        offset_y = 15

        # Check if click is within the board
        if offset_x <= x <= offset_x + 720 and offset_y <= y <= offset_y + 720:
            # Calculate row and column
            row = (y - offset_y) // cell_size
            col = (x - offset_x) // cell_size
            return row, col
        else:
            return None
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
        """
        Places the value in the selected cell.
        """

        if self.selected_cell is not None:
            row, col = self.selected_cell
            # Check if the cell is empty
            if self.board[row][col] == 0:
                self.board[row][col] = value

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row, col = self.click(x, y)
                self.select_cell(row, col)
            elif event.type == pygame.KEYDOWN:
                if pygame.K_1 <= event.key <= pygame.K_9:
                    value = event.key - pygame.K_0
                    self.place_number(value)

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

