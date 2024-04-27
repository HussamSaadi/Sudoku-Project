import pygame
import sys
import button
# import menu
# from menu import draw_text
pygame.init()

width, height = 800, 800
screen = pygame.display.set_mode((width, height))

# define colors + font
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen.fill(WHITE)
font = pygame.font.SysFont("arialblack", 60)

# image
img = pygame.image.load('buttonIcons/confetti.jpeg')
r = img.get_rect()
r.center = screen.get_rect().center
screen.blit(img, r)

pygame.display.flip()
def draw_text(screen, text, font, text_col, x, y):
    screen_text = font.render(text, True, text_col)
    screen.blit(screen_text, (x,y))

# load images
exit_img = pygame.image.load('buttonIcons/exit.png').convert_alpha()

exit_button = button.Button(323, 420, exit_img, 0.7)

# run loop
run = True
while run:
    draw_text(screen,"Game won!", font, BLACK, 220, 300)

    if exit_button.draw(screen):
        print("Exit!")
        pygame.quit()
        sys.exit()
    for event in pygame.event.get():
        # if event.type == pygame.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

