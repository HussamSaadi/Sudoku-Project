import pygame
import sys

# initialize pygame
pygame.init()

# Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
# Draws every cell on this board.
pink = (255, 182, 193)
white = (255, 255, 255)

# Set the window dimensions
WINDOW_SIZE = (500, 500)

# display screen
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Sudoku Grid")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

screen.fill(pink)

# Draw grid


# Update the display
# pygame.display.flip()