import pygame
import sys
from board import *

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 750, 750
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sudoku Grid")

# Define colors
PINK = (255, 182, 193)

def main():
    sudoku_board = Board(width, height, screen, difficulty="medium")

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Get the position of the mouse click
                x, y = pygame.mouse.get_pos()
                # Check if a cell was clicked
                clicked_cell = sudoku_board.click(x, y)
                if clicked_cell:
                    # Update the selected cell
                    sudoku_board.select(*clicked_cell)  # Unpack the tuple
                    print("Clicked cell:", clicked_cell)  # For debugging purposes
            elif event.type == pygame.KEYDOWN:
                # Handle keyboard input
                if pygame.K_1 <= event.key <= pygame.K_9:  # Check if the pressed key is a number key
                    value = event.key - pygame.K_0  # Convert key code to integer value
                    # Place the value in the selected cell
                    sudoku_board.place_number(value)

        # Update the display
        sudoku_board.draw()
        pygame.display.flip()

if __name__ == "__main__":
    main()