import pygame
import sys
from board import *
from cell import *
from sudoku_generator import *

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
# font = pygame.font.SysFont("arialblack", 40)
pygame.display.set_caption("SUDOKU")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PINK = (255, 174, 201, 255)
BLUE = (0, 162, 232, 255)
LIGHT_BLUE = (173, 216, 230)

def main():

    easy, medium, hard = "easy", "medium", "hard"
    sudoku_board = Board(width, height, screen, difficulty="medium")

    # Generate initial board
    generated_board = generate_sudoku(9, 40)

    for row in range(9):
        for col in range(9):
            value = generated_board[row][col]
            if value != 0:
                sudoku_board.cells[row][col].set_cell_value(value)

    running = True
    while running:
        sudoku_board.draw()
        sudoku_board.handle_events()
        # if sudoku_board.is_full():
        #     print("Congratulations! You have solved the Sudoku!")
        #     running = False

if __name__ == "__main__":
    main()















# import pygame
# import sys
# from board import *
# from cell import *
# from sudoku_generator import *
#
# # Initialize Pygame
# pygame.init()
#
# # Set up the display
# width, height = 750, 750
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption("SUDOKU")
#
# # Define colors
#
#
# def main():
#     sudoku_board = Board(width, height, screen, difficulty="medium")
#
#     sudoku_generator = SudokuGenerator(9, 45)
#     sudoku_generator.fill_values()
#     sudoku_generator.remove_cells()
#
#     generated_board = sudoku_generator.get_board()
#     for row in range(9):
#         for col in range(9):
#             value = generated_board[row][col]
#             if value != 0:
#                 sudoku_board.cells[row][col].set_sketched_value(value)
#
#     running = True
#     while running:
#         sudoku_board.draw()
#         sudoku_board.handle_events()
#         if sudoku_board.is_full():
#             print("Congratulations! You have solved the Sudoku!")
#             running = False
#
# if __name__ == "__main__":
#     main()
