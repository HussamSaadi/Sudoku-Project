import pygame
import sys

pygame.init()
# Set the width and height of the window
width, height = 750, 750
window_size = (width, height)

# Create a window
window = pygame.display.set_mode(window_size)
# pygame.display.set_caption("Individual Squares")

# Set the color of the square
PINK = (255, 182, 193)
BLACK = (0, 0, 0)
square_color = BLACK

class Cell:
    def __init__(self, value, row, col , screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.font = pygame.font.Font(None, 65)
        self.selected = False
        self.square_height = (720 // 9) ** 0.5
        self.square_width = (720 // 9) ** 0.5
        self.x_location = col * self.square_width
        self.y_location = row * self.square_height
        self.red = (255, 0, 0)
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.beige = (245, 245, 220)
        pass

    def set_cell_value(self, value):
        self.cell_value = value
        pass

    def set_sketched_value(self, value):
        self.skectech_value = value
        pass

    def draw(self):
        if self.selected:



        # Set the size and position of the square
        # FIRST WORKED OUT
        # square_size = 80
        # square_position = (15, 15)  # Top left corner
        # line_width = 5
        #
        # # Main loop
        # while True:
        #     # Handle events
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             pygame.quit()
        #             sys.exit()
        #
        #     # Fill the window with white color
        #     window.fill(PINK)
        #
        #     # Draw the square
        #     pygame.draw.rect(window, square_color, (square_position, (square_size, square_size)), line_width)
        #
        #     # Update the display
        #     pygame.display.flip()





    # while (i * 80) < 720:
    # pygame.draw.line(screen, BLACK, pygame.Vector2(((i * 80) + 15), 15), pygame.Vector2(((i * 80) + 15), 15), 5)
    #Draws this cell, along with the value inside it.
    # If this cell has a nonzero value, that value is displayed.
    #     if 0 <= self.value <= 9:
    #         size = [self.row, self.col]
    #         white = (255, 255, 255)
    #         screen_display = pygame.display
    #         surface = screen_display.set_mode(size)
    #         pygame.draw.rect(surface, white, pygame.Rect(30, 30, 60, ))

            # text_font = pygame.font.SysFont(text_type, size)
            # text_render = text_font.render(text, True, color)
            # rect_dims = list(pygame.Surface.get_rect(text_render))

            # pygame.Surface.blit()
            # cell = pygame.Surface.get_rect()
            # draw = pygame.draw.rect(cell)
    # Otherwise, no value is displayed in the cell.


        # get_rect()
        # get rect size, then render
        # to center, divide size by 2
        # multiply the square size by the number of the column/row to move it there
        # each square will have a size of one
        # text_surface = my_font.render('Some Text', False, (0, 0, 0))
        # prev. line (change 0's to black)
        # get dim, center with get_rect(), then blit


