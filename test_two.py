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