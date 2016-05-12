# Dr. Snake 2
# Eric Olenski
# 4-7-16
 
import pygame

class LeftSnake():

    ''' Controls Every thing for the left snake.'''

    def __init__(self):
        self.height = 18
        self.width = 18
        self.length = 1
        self.head_x = 41
        self.head_y = 221

    def draw_head(self, x, y, color):
        self.head_x = x
        self.head_y = y
        
    def get_x(self):
        return self.head_x

    def get_y(self):
        return self.head_y

    def get_length(self):
        return self.length
        
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (50, 205, 50)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BROWN = (84, 46, 23)
YELLOW = (255, 255, 0)
SKY = (168, 255, 255)
GREY = (170, 170, 170)

PI = 3.141592653
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (1600, 1000)
screen = pygame.display.set_mode(size)

# Grid height and width and margin
HEIGHT = 18
WIDTH = 18
MARGIN = 2

# Set up the Array for grid
leftGrid = []
for row in range(39):
    leftGrid.append([])
    for column in range(38):
        leftGrid[row].append(0)

leftGrid[1][1] = 1

leftSnake = LeftSnake()
leftx = leftSnake.get_x()
lefty = leftSnake.get_y()
leftxSpeed = 0
leftySpeed = 0
leftColor = YELLOW
 
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

        # Movement of the left snake  
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                for xy in leftLength:
                    x = xy[0]
                    y = xy[1]
                    leftGrid[x][y] = 0
                    y -= 1
                    leftGrid[x][y] = 1
                
            elif event.key == pygame.K_d:
                for xy in leftLength:
                    x = xy[0]
                    y = xy[1]
                    leftGrid[x][y] = 0
                    y += 1
                    leftGrid[x][y] = 1
                
            elif event.key == pygame.K_w:
                for xy in leftLength:
                    x = xy[0]
                    y = xy[1]
                    leftGrid[x][y] = 0
                    x -= 1
                    leftGrid[x][y] = 1
                
            elif event.key == pygame.K_s:
                for xy in leftLength:
                    x = xy[0]
                    y = xy[1]
                    leftGrid[x][y] = 0
                    x += 1
                    leftGrid[x][y] = 1

    # Splits the screen
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, [0, 200, 1600, 800])

    # Game play walls
    pygame.draw.rect(screen, RED, [0, 180, 1600, 20])
    pygame.draw.rect(screen, RED, [0, 200, 20, 800])
    pygame.draw.rect(screen, RED, [0, 980, 1600, 20])
    pygame.draw.rect(screen, RED, [1580, 200, 20, 800])
    pygame.draw.rect(screen, RED, [780, 200, 40, 800])

    # Draw snakes
    leftLength = []
    for row in range(39):
        for column in range(38):
            color = BLACK
            if leftGrid[row][column] == 1:
                color = YELLOW
                leftLength.append([row, column])
            pygame.draw.rect(screen, color,
                             [(MARGIN + WIDTH) * column + MARGIN + 20,
                              (MARGIN + HEIGHT) * row + MARGIN + 200,
                              WIDTH,
                              HEIGHT])

    pygame.display.flip()
 
    clock.tick(60)

# Close the window and quit.
pygame.quit()
