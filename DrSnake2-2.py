# Dr. Snake 1
# Eric Olenski
# 3-3-16
 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (50, 205, 50)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BROWN = (84, 46, 23)
YELLOW = (255, 255, 0)
SKY = (168, 255, 255)

PI = 3.141592653
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (1600, 1000)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Dr. Snake")
 
# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Splits the screen
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, [0, 200, 1600, 800])

    # Game play walls
    pygame.draw.rect(screen, RED, [0, 180, 1600, 20])
    pygame.draw.rect(screen, RED, [0, 200, 20, 800])
    pygame.draw.rect(screen, RED, [0, 980, 1600, 20])
    pygame.draw.rect(screen, RED, [1580, 200, 20, 800])
    pygame.draw.rect(screen, RED, [780, 200, 40, 800])

    pygame.display.flip()
 
    clock.tick(60)

# Close the window and quit.
pygame.quit()
