import pygame
import sys

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PINK = (255, 174, 201, 255)
BLUE = (0, 162, 232, 255)


class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.font = pygame.font.Font(None, 65)
        self.selected = False

    def set_cell_value(self, value):
        self.value = value
        print(value)

    def set_sketched_value(self, value):
        self.sketched_value = value
        print(value)

    def draw(self):
        cell_size = 720 // 9
        offset_x = 15
        offset_y = 15
        cell_rect = pygame.Rect(self.col * cell_size + offset_x, self.row * cell_size + offset_y, cell_size, cell_size)
        pygame.draw.rect(self.screen, WHITE, cell_rect)
        pygame.draw.rect(self.screen, BLUE, cell_rect, 1)
        # Add red boundary if the cell is selected
        if self.selected:
            pygame.draw.rect(self.screen, PINK, (
            (self.col * cell_size) + offset_x, (self.row * cell_size) + offset_y, cell_size, cell_size))
        if self.value != 0:
            text_surface = self.font.render(str(self.value), True, BLACK)
            text_rect = text_surface.get_rect(center=cell_rect.center)
            self.screen.blit(text_surface, text_rect)
