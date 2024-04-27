import pygame
import sys
import button
from sudoku_test import main_menu

from pygame.locals import *


class menu:
    def __init__(self):
        pygame.init()

        # create game window
        width = 800
        height = 800
        self.set_level = 0

        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Main Menu")

        # define colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.screen.fill(self.WHITE)

        # define fonts
        self.font = pygame.font.SysFont("arialblack", 40)

        # game variables
        # menu_state = "main"

        # create surface object, image is drawn on it
        img = pygame.image.load('buttonIcons/main.png')
        r = img.get_rect()
        r.center = self.screen.get_rect().center
        vertical_offset = 50
        r.y -= vertical_offset
        # scaled_img = pygame.transform.scale(img, (700, 700))
        self.screen.blit(img, r)

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

        run = True
        while run:
            # check menu state
            # if menu_state == "main":
            if easy_button.draw(self.screen):
                self.set_level = 30
                print("Easy")
                main()
                # menu_state = "new screen"
            if med_button.draw(self.screen):
                self.set_level = 40
                print("Medium")
                main()
            if hard_button.draw(self.screen):
                self.set_level = 50
                print("Hard")
                main()
            # menu_state = "main"

            # draw_text("Welcome to Sudoku", font, BLACK, 185, 70)
            # draw_text("Select Game Mode:", font, BLACK, 185, 565)
            # for event in pygame.event.get():
            #     # if event.type == pygame.
            #     if event.type == pygame.QUIT:
            #         pygame.quit()
            #         sys.exit()
            # pygame.display.update()

    def level_grab(self):
        return self.set_level

    def draw_text(self, text, font, text_col, x, y):
        screen_text = font.render(text, True, text_col)
        self.screen.blit(screen_text, (x, y))

    def final_draw(self):
        self.draw_text("Welcome to Sudoku", self.font, self.BLACK, 185, 70)
        self.draw_text("Select Game Mode:", self.font, self.BLACK, 185, 565)
        for event in pygame.event.get():
            # if event.type == pygame.
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        print()

# def run_menu():
#     # game loop
#     run = True
#     while run:
#         # check menu state
#         # if menu_state == "main":
#         if easy_button.draw(screen):
#             set_level = 30
#             print("Easy")
#             main()
#             # menu_state = "new screen"
#         if med_button.draw(screen):
#             set_level = 40
#             print("Medium")
#             main()
#         if hard_button.draw(screen):
#             set_level = 50
#             print("Hard")
#             main()
#         # menu_state = "main"
#
#         draw_text("Welcome to Sudoku", font, BLACK, 185, 70)
#         draw_text("Select Game Mode:", font, BLACK, 185, 565)
#         for event in pygame.event.get():
#             # if event.type == pygame.
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#         pygame.display.update()
