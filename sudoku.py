import pygame, sys
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

# MM BG image
img1 = pygame.image.load('buttonIcons/main.png')
r = img1.get_rect()
r.center = screen.get_rect().center
vertical_offset = 20
r.y -= vertical_offset

# congrats BG image
img2 = pygame.image.load('buttonIcons/confetti.jpeg')
r2 = img2.get_rect()
r2.center = screen.get_rect().center
vertical_offset2 = 50
r2.y -= vertical_offset

# game over BG image
img3 = pygame.image.load('buttonIcons/sad_face2.jpeg')
r3 = img3.get_rect()
r3.center = screen.get_rect().center
vertical_offset3 = 50
r3.y -= vertical_offset

# define fonts
font = pygame.font.SysFont("arialblack", 40)

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PINK = (255, 174, 201, 255)
BLUE = (0, 162, 232, 255)
LIGHT_BLUE = (173, 216, 230)


def main_menu():  # main menu screen
    pygame.display.set_caption("Sudoku")

    # load button images
    easy_img = pygame.image.load('buttonIcons/easyB.png').convert_alpha()
    med_img = pygame.image.load('buttonIcons/mediumB.png').convert_alpha()
    hard_img = pygame.image.load('buttonIcons/hardB.png').convert_alpha()

    # create button instances
    easy_button = button.Button(153, 670, easy_img, 0.7)
    med_button = button.Button(323, 670, med_img, 0.7)
    hard_button = button.Button(493, 670, hard_img, 0.7)

    def draw_text(text, font, text_col, x, y):
        screen_text = font.render(text, True, text_col)
        screen.blit(screen_text, (x, y))

    while True:
        screen.fill(WHITE)
        screen.blit(img1, r)  # or (0,0)

        draw_text("Welcome to Sudoku", font, BLACK, 185, 90)
        draw_text("Select Game Mode:", font, BLACK, 185, 600)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if easy_button.draw(screen):
                set_level = 1
                print("Easy")
                return set_level
                # menu_state = "new screen"
            if med_button.draw(screen):
                set_level = 40
                print("Medium")
                return set_level
                # main()
            if hard_button.draw(screen):
                set_level = 50
                print("Hard")
                return set_level
        # draw buttons
        easy_button.draw(screen)
        med_button.draw(screen)
        hard_button.draw(screen)

        pygame.display.update()

    # displays congrats screen if user solves board correctly
def congrats():
    def draw_text(screen, text, font, text_col, x, y):
        screen_text = font.render(text, True, text_col)
        screen.blit(screen_text, (x, y))

    while True:
        screen.fill(WHITE)
        screen.blit(img2, r2)

        # load images
        exit_img = pygame.image.load('buttonIcons/exit.png').convert_alpha()

        # create button instances
        exit_button = button.Button(323, 420, exit_img, 0.7)

        draw_text(screen, "Game won!", font, BLACK, 270, 300)

        for event in pygame.event.get():
            # if event.type == pygame.
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if exit_button.draw(screen):
                print("Exit!")
                pygame.quit()
                sys.exit()
            # draw buttons
        exit_button.draw(screen)

        pygame.display.update()

def game_over():
    def draw_text(screen, text, font, text_col, x, y):
        screen_text = font.render(text, True, text_col)
        screen.blit(screen_text, (x, y))

    while True:
        screen.fill(WHITE)
        screen.blit(img3, r3)

        # load images
        restart_img = pygame.image.load('buttonIcons/restart.png').convert_alpha()

        restart_button = button.Button(323, 650, restart_img, 0.7)
        draw_text(screen, "Game over", font, BLACK, 280, 75)
        # restart_game = False

        for event in pygame.event.get():
            # if event.type == pygame.
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if restart_button.draw(screen):
                print("Restart")
                main_menu()
                # restart_game = True
        # draw buttons
        restart_button.draw(screen)

        pygame.display.update()
# def second_main(set_level):
#
#     return sudoku_board
def main():

    set_level = main_menu()
    sudoku_board = Board(width, height, screen, set_level)
    # Generate initial board
    # generated_board = generate_sudoku(9, 3)
    generated_board = sudoku_board.generated_board_grab()

    for row in range(9):
        for col in range(9):
            value = generated_board[row][col]
            if value != 0:
                sudoku_board.cells[row][col].set_cell_value(value)

    # load button images
    reset_img = pygame.image.load('buttonIcons/reset.png').convert_alpha()
    restart_img = pygame.image.load('buttonIcons/restart.png').convert_alpha()
    exit_img = pygame.image.load('buttonIcons/exit.png').convert_alpha()

    # create button instances
    reset_button = button.Button(153, 730, reset_img, 0.7)
    restart_button = button.Button(323, 730, restart_img, 0.7)
    exit_button = button.Button(493, 730, exit_img, 0.7)

    # main_menu()

    # sudoku_board = second_main(set_level)

    running = True

    while running:
        sudoku_board.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Handle mouse click events
                x, y = pygame.mouse.get_pos()
                # Handle button clicks
                if reset_button.rect.collidepoint(x, y):
                    print("Reset")
                elif restart_button.rect.collidepoint(x, y):
                    print("Restart")
                elif exit_button.rect.collidepoint(x, y):
                    print("Exit")
                    pygame.quit()
                    sys.exit()
                else:
                    # Handle cell clicks
                    row, col = sudoku_board.click(x, y)
                    sudoku_board.select(row, col)
            elif event.type == pygame.KEYDOWN:
                # Handle key presses
                if pygame.K_1 <= event.key <= pygame.K_9:
                    print("Number key pressed")
                    value = event.key - pygame.K_0
                    sudoku_board.place_number(value)
                elif event.key == pygame.K_BACKSPACE:
                    print("Delete key pressed")
                    sudoku_board.clear()
        # sudoku_board.handle_events()
        if sudoku_board.is_full():
            final_destination = sudoku_board.check_board()
            if final_destination:
                # game_over_screen = game_over()
                congrats_screen = congrats()
                # if game_over_screen:
                if congrats_screen:
                    continue
                print("Congratulations! You have solved the Sudoku!")
            else:
                print("Wrong! You solved it wrong!")
                running = False
                # Draw buttons
        reset_button.draw(sudoku_board.screen)
        restart_button.draw(sudoku_board.screen)
        exit_button.draw(sudoku_board.screen)

    pygame.display.flip()

if __name__ == "__main__":
    main()

# import pygame, sys
# from board import *
# # from cell import *
# from sudoku_generator import *
# # import button
# # from menu_2 import *
#
# # Initialize Pygame
# pygame.init()
#
# # Set up the display
# width, height = 800, 800
# screen = pygame.display.set_mode((width, height))
#
# # MM BG image
# img1 = pygame.image.load('buttonIcons/main.png')
# r = img1.get_rect()
# r.center = screen.get_rect().center
# vertical_offset = 20
# r.y -= vertical_offset
#
# # congrats BG image
# img2 = pygame.image.load('buttonIcons/confetti.jpeg')
# r2 = img2.get_rect()
# r2.center = screen.get_rect().center
# vertical_offset2 = 50
# r2.y -= vertical_offset
#
# # game over BG image
# img3 = pygame.image.load('buttonIcons/sad_face2.jpeg')
# r3 = img3.get_rect()
# r3.center = screen.get_rect().center
# vertical_offset3 = 50
# r3.y -= vertical_offset
#
# # define fonts
# font = pygame.font.SysFont("arialblack", 40)
#
# # Define colors
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# PINK = (255, 174, 201, 255)
# BLUE = (0, 162, 232, 255)
# LIGHT_BLUE = (173, 216, 230)
#
# def main_menu(): # main menu screen
#     pygame.display.set_caption("Sudoku")
#
#     # load button images
#     easy_img = pygame.image.load('buttonIcons/easyB.png').convert_alpha()
#     med_img = pygame.image.load('buttonIcons/mediumB.png').convert_alpha()
#     hard_img = pygame.image.load('buttonIcons/hardB.png').convert_alpha()
#
#     # create button instances
#     easy_button = button.Button(153, 670, easy_img, 0.7)
#     med_button = button.Button(323, 670, med_img, 0.7)
#     hard_button = button.Button(493, 670, hard_img, 0.7)
#
#     def draw_text(text, font, text_col, x, y):
#         screen_text = font.render(text, True, text_col)
#         screen.blit(screen_text, (x, y))
#
#     while True:
#         screen.fill(WHITE)
#         screen.blit(img1, r) # or (0,0)
#
#         draw_text("Welcome to Sudoku", font, BLACK, 185, 90)
#         draw_text("Select Game Mode:", font, BLACK, 185, 600)
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if easy_button.draw(screen):
#                 set_level = 1
#                 print("Easy")
#                 second_main(set_level)
#                 # menu_state = "new screen"
#             if med_button.draw(screen):
#                 set_level = 40
#                 print("Medium")
#                 second_main(set_level)
#                 # main()
#             if hard_button.draw(screen):
#                 set_level = 50
#                 print("Hard")
#                 second_main(set_level)
#         # draw buttons
#         easy_button.draw(screen)
#         med_button.draw(screen)
#         hard_button.draw(screen)
#
#         pygame.display.update()
#
# # displays congrats screen if user solves board correctly
# def congrats():
#     def draw_text(screen, text, font, text_col, x, y):
#         screen_text = font.render(text, True, text_col)
#         screen.blit(screen_text, (x, y))
#
#     while True:
#         screen.fill(WHITE)
#         screen.blit(img2, r2)
#
#         # load images
#         exit_img = pygame.image.load('buttonIcons/exit.png').convert_alpha()
#
#         # create button instances
#         exit_button = button.Button(323, 420, exit_img, 0.7)
#
#         draw_text(screen, "Game won!", font, BLACK, 270, 300)
#
#         for event in pygame.event.get():
#             # if event.type == pygame.
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if exit_button.draw(screen):
#                 print("Exit!")
#                 pygame.quit()
#                 sys.exit()
#         # draw buttons
#         exit_button.draw(screen)
#
#         pygame.display.update()
#
# def game_over():
#     def draw_text(screen, text, font, text_col, x, y):
#         screen_text = font.render(text, True, text_col)
#         screen.blit(screen_text, (x, y))
#
#     while True:
#         screen.fill(WHITE)
#         screen.blit(img3, r3)
#
#         # load images
#         restart_img = pygame.image.load('buttonIcons/restart.png').convert_alpha()
#
#         restart_button = button.Button(323, 650, restart_img, 0.7)
#         draw_text(screen, "Game over", font, BLACK, 280, 75)
#         # restart_game = False
#
#         for event in pygame.event.get():
#             # if event.type == pygame.
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if restart_button.draw(screen):
#                 print("Restart")
#                 main()
#                 # restart_game = True
#         # draw buttons
#         restart_button.draw(screen)
#
#         pygame.display.update()
#
# def second_main(set_level):
#     sudoku_board = Board(width, height, screen, set_level)
#
#     # Generate initial board
#     # generated_board = generate_sudoku(9, 3)
#     generated_board = sudoku_board.generated_board_grab()
#
#     for row in range(9):
#         for col in range(9):
#             value = generated_board[row][col]
#             if value != 0:
#                 sudoku_board.cells[row][col].set_cell_value(value)
#
#     running = True
#     while running:
#         sudoku_board.draw()
#         pygame.display.flip()
#
#         # sudoku_board.handle_events()
#         if sudoku_board.is_full():
#
#             final_destination = sudoku_board.check_board()
#             if final_destination == True:
#                 # game_over_screen = game_over()
#                 congrats_screen = congrats()
#                 #if game_over_screen:
#                 if congrats_screen:
#                     continue
#
#                 print("Congratulations! You have solved the Sudoku!")
#             else:
#                 print("Wrong! You solved it wrong!")
#             running = False
#
# if __name__ == "__main__":
#     main()