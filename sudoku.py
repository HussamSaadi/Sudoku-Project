import pygame
import sys
from board import *
from cell import *
from sudoku_generator import *
import button
from menu_2 import *

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
# font = pygame.font.SysFont("arialblack", 1)
pygame.display.set_caption("SUDOKU")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PINK = (255, 174, 201, 255)
BLUE = (0, 162, 232, 255)
LIGHT_BLUE = (173, 216, 230)

def main():
    pygame.init()

    # create game window
    width = 800
    height = 800

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Main Menu")

    # define colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    screen.fill(WHITE)

    # define fonts
    font = pygame.font.SysFont("arialblack", 40)

    # game variables
    # menu_state = "main"

    # create surface object, image is drawn on it
    img = pygame.image.load('buttonIcons/main.png')
    r = img.get_rect()
    r.center = screen.get_rect().center
    vertical_offset = 50
    r.y -= vertical_offset
    # scaled_img = pygame.transform.scale(img, (700, 700))
    screen.blit(img, r)

    # load button images
    easy_img = pygame.image.load('buttonIcons/easyB.png').convert_alpha()
    med_img = pygame.image.load('buttonIcons/mediumB.png').convert_alpha()
    hard_img = pygame.image.load('buttonIcons/hardB.png').convert_alpha()

    # button class
    # class Button:
    #     def __init__(self, x, y, image, scale):
    #         width = image.get_width()
    #         height = image.get_height()
    #         self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
    #         self.rect = self.image.get_rect()
    #         self.rect.topleft = (x, y)
    #         self.clicked = False
    #
    #     def draw(self):
    #         action = False
    #         # get mouse position
    #         pos = pygame.mouse.get_pos()
    #
    #         # check mouseover and clicked conditions
    #         if self.rect.collidepoint(pos):
    #             if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
    #                 self.clicked = True
    #                 action = True
    #         if pygame.mouse.get_pressed()[0] == 0:
    #             self.clicked = False
    #
    #         # draw button on screen
    #         screen.blit(self.image, (self.rect.x, self.rect.y))
    #
    #         return action

    # create button instances
    easy_button = button.Button(153, 650, easy_img, 0.7)
    med_button = button.Button(323, 650, med_img, 0.7)
    hard_button = button.Button(493, 650, hard_img, 0.7)

    pygame.display.flip()

    def draw_text(text, font, text_col, x, y):
        screen_text = font.render(text, True, text_col)
        screen.blit(screen_text, (x, y))

    # game loop
    run = True
    while run:
        # check menu state
        # if menu_state == "main":
        if easy_button.draw(screen):
            set_level = 1
            print("Easy")
            second_main(set_level)
            # menu_state = "new screen"
        if med_button.draw(screen):
            set_level = 40
            print("Medium")
            second_main(set_level)
            # main()
        if hard_button.draw(screen):
            set_level = 50
            print("Hard")
            second_main(set_level)
            # main()
        # menu_state = "main"

        draw_text("Welcome to Sudoku", font, BLACK, 185, 70)
        draw_text("Select Game Mode:", font, BLACK, 185, 565)
        for event in pygame.event.get():
            # if event.type == pygame.
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

    # start_menu = menu()
    # start_menu.draw_text()
    # start_menu.final_draw()
    # user_level = start_menu.level_grab()

    # easy, medium, hard = "easy", "medium", "hard"

def second_main(set_level):
    sudoku_board = Board(width, height, screen, set_level)

    # Generate initial board
    # generated_board = generate_sudoku(9, 3)
    generated_board = sudoku_board.generated_board_grab()

    for row in range(9):
        for col in range(9):
            value = generated_board[row][col]
            if value != 0:
                sudoku_board.cells[row][col].set_cell_value(value)

    running = True
    while running:

        sudoku_board.draw()
        pygame.display.flip()

        # sudoku_board.handle_events()
        if sudoku_board.is_full():

            final_destination = sudoku_board.check_board()
            if final_destination == False:

                print("Congratulations! You have solved the Sudoku!")
            else:
                print("Wrong! You solved it wrong!")
            running = False

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
