from board import *
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
new_board = Board(width, height, screen, difficulty="medium")
