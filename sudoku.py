import pygame
from board import Board
from sudoku_generator import *

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont("arialblack", 40)
pygame.display.set_caption("SUDOKU")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PINK = (255, 174, 201, 255)
BLUE = (0, 162, 232, 255)
LIGHT_BLUE = (173, 216, 230)


def main():
    sudoku_board = Board(width, height, screen, difficulty="medium")

    print("Sudoku board created")

    sudoku_generator = SudokuGenerator(9, 45)
    print("1")
    sudoku_generator.fill_values()
    print("2s")
    sudoku_generator.remove_cells()
    print("Sudoku board generated")

    generated_board = sudoku_generator.get_board()
    for row in range(9):
        for col in range(9):
            value = generated_board[row][col]
            if value != 0:
                sudoku_board.cells[row][col].set_sketched_value(value)

    running = True
    while running:
        sudoku_board.draw()
        # sudoku_board.handle_events()

        pygame.display.flip()
        if sudoku_board.is_full():
            running = False
    print("Game loop exited")

if __name__ == "__main__":
    main()

