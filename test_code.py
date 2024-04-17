import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame Test")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Box dimensions and position
box_width = 100
box_height = 100
box_x = (800 - box_width) // 2
box_y = (600 - box_height) // 2

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with white color
    screen.fill(WHITE)

    # Draw a red box
    pygame.draw.rect(screen, RED, (box_x, box_y, box_width, box_height))

    # Update the display
    pygame.display.flip()