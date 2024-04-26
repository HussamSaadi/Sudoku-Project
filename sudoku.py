import pygame
import sys
from board import *
from cell import *
from new_example_file import *

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 750, 750
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("SUDOKU")

# Define colors


def main():
    sudoku_board = Board(width, height, screen, difficulty="medium")
    generated_board = generate_sudoku(9, 45)  # Change the parameters as needed
    for row in range(9):
        for col in range(9):
            value = generated_board[row][col]
            if value != 0:
                sudoku_board.cells[row][col].set_sketched_value(value)


    # Main game loop
    running = True
    while running:

        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         running = False
        sudoku_board.handle_events()
        sudoku_board.draw()
        pygame.display.flip()

if __name__ == "__main__":
    main()
