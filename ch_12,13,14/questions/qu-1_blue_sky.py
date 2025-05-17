import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants for the window dimensions
WIDTH = 800
HEIGHT = 600

# Create the Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the window title
pygame.display.set_caption("Blue Background")

# Define the blue color (R, G, B)
BLUE = (0, 0, 255)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with the blue color
    screen.fill(BLUE)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()
