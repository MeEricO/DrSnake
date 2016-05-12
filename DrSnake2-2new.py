# Dr. Snake 2-2
# Eric Olenski
# 4-12-16
 
import pygame
from Walls import Wall
from LeftSnake import LeftSnake
from RightSnake import RightSnake
 
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
screenHeight = 800
screenWidth = 1600
size = (screenWidth, screenHeight)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Dr. Snake")

# ---------------------Walls----------------------------
wallList = pygame.sprite.Group()

# Left side walls---------------------------------------
# Left------------------------
wall = Wall(0, 0, 20, 800)
wallList.add(wall)

# Top-------------------------
wall = Wall(0, 0, 800, 20)
wallList.add(wall)

# Bottom----------------------
wall = Wall(0, 780, 800, 20)
wallList.add(wall)

# Right-----------------------
wall = Wall(780, 0, 20, 800)
wallList.add(wall)

# Right side walls--------------------------------------
# Left------------------------
wall = Wall(800, 0, 20, 800)
wallList.add(wall)

# Top-------------------------
wall = Wall(800, 0, 800, 20)
wallList.add(wall)

# Bottom----------------------
wall = Wall(800, 780, 800, 20)
wallList.add(wall)

# Right-----------------------
wall = Wall(1580, 0, 20, 800)
wallList.add(wall)
# ------------------------------------------------------

# ---------------------Snakes---------------------------
snakeWidth = 18
snakeHeight = 18
margin = 2
# Left--------------------------------------------------
leftSnakeList = pygame.sprite.Group()
leftSnake = LeftSnake(40, 40)
leftSnakeList.add(leftSnake)
# Right-------------------------------------------------
rightSnakeList = pygame.sprite.Group()
rightSnake = LeftSnake(840, 40)
rightSnakeList.add(rightSnake)
# ------------------------------------------------------

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
    pygame.draw.rect(screen, BLACK, [0, 0, 1600, 800])

    # Game play walls
    wallList.draw(screen)

    # Snakes
    leftSnakeList.draw(screen)
    rightSnakeList.draw(screen)

    pygame.display.flip()
 
    clock.tick(5)

# Close the window and quit.
pygame.quit()
