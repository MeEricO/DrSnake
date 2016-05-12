# Dr. Snake 4
# Eric Olenski
# 4-14-16
 
import pygame
import random
from Walls import Wall
from LeftSnake import LeftSnake
from RightSnake import RightSnake
from LeftRedBLocks import LeftRedBLock
from RightRedBlock import RightRedBLock
 
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
allSpritesList = pygame.sprite.Group()
hitList = pygame.sprite.Group()

# ---------------------Walls----------------------------
wallList = []

# Left side walls---------------------------------------
# Left------------------------
wall = Wall(0, 0, 20, 800)
wallList.insert(0, wall)

# Top-------------------------
wall = Wall(0, 0, 800, 20)
wallList.insert(0, wall)

# Bottom----------------------
wall = Wall(0, 780, 800, 20)
wallList.insert(0, wall)

# Right-----------------------
wall = Wall(780, 0, 20, 800)
wallList.insert(0, wall)

# Right side walls--------------------------------------
# Left------------------------
wall = Wall(800, 0, 20, 800)
wallList.insert(0, wall)

# Top-------------------------
wall = Wall(800, 0, 800, 20)
wallList.insert(0, wall)

# Bottom----------------------
wall = Wall(800, 780, 800, 20)
wallList.insert(0, wall)

# Right-----------------------
wall = Wall(1580, 0, 20, 800)
wallList.insert(0, wall)

allSpritesList.add(wallList)
# ------------------------------------------------------

# ---------------------Snakes---------------------------
snakeWidth = 18
snakeHeight = 18
margin = 2
# Initial speed------------------------
leftxChange = 0
leftyChange = 0
rightxChange = 0
rightyChange = 0
# Left---------------------------------
leftSnakeList = []
leftSnake = LeftSnake(40, 40)
leftSnakeList.insert(0, leftSnake)
allSpritesList.add(leftSnake)
# Right--------------------------------
rightSnakeList = []
rightSnake = LeftSnake(840, 40)
rightSnakeList.insert(0, rightSnake)
allSpritesList.add(rightSnake)
# ------------------------------------------------------

# -------------------Red Blocks-------------------------
# Initial red block left------------------------
leftRedHits = pygame.sprite.Group()
leftRedList = pygame.sprite.Group()
totalLeftReds = 0
leftRedx = random.randint(20, 760)
while leftRedx % 20 != 0:
    leftRedx = random.randint(20, 760)
leftRedy = random.randint(20, 760)
while leftRedy % 20 != 0:
    leftRedy = random.randint(20, 760)
leftRed = LeftRedBLock(leftRedx, leftRedy)
allSpritesList.add(leftRed)
leftRedList.add(leftRed)

# Initial red block right------------------------
rightRedHits = pygame.sprite.Group()
rightRedList = pygame.sprite.Group()
totalightReds = 0
rightRedx = random.randint(820, 1560)
while rightRedx % 20 != 0:
    rightRedx = random.randint(820, 1560)
rightRedy = random.randint(20, 760)
while rightRedy % 20 != 0:
    rightRedy = random.randint(20, 760)
rightRed = RightRedBLock(rightRedx, rightRedy)
allSpritesList.add(rightRed)
rightRedList.add(rightRed)
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

        # ------------------Movement of snakes-----------------------------
        # Set left snakes direction----------------------
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                leftxChange = (snakeWidth + margin) * -1
                leftyChange = 0
                xNew = -1
                yNew = 0

            elif event.key == pygame.K_d:
                leftxChange = (snakeWidth + margin)
                leftyChange = 0
                xNew = 1
                yNew = 0
                
            elif event.key == pygame.K_w:
                leftxChange = 0
                leftyChange = (snakeWidth + margin) * -1
                xNew = 0
                yNew = -1
                
            elif event.key == pygame.K_s:
                leftxChange = 0
                leftyChange = (snakeWidth + margin)
                xNew = 0
                yNew = 1

        # Set right snake direction---------------------
            if event.key == pygame.K_LEFT:
                rightxChange = (snakeWidth + margin) * -1
                rightyChange = 0

            elif event.key == pygame.K_RIGHT:
                rightxChange = (snakeWidth + margin)
                rightyChange = 0
                
            elif event.key == pygame.K_UP:
                rightxChange = 0
                rightyChange = (snakeWidth + margin) * -1
                
            elif event.key == pygame.K_DOWN:
                rightxChange = 0
                rightyChange = (snakeWidth + margin)

    # Make left snake move------------------------------
    hitList = pygame.sprite.spritecollide(leftSnake, wallList, False)
    for block in hitList:
        pygame.quit()
        
    if len(leftSnakeList) > 1:
        length = len(leftSnakeList)
        for seg in range(length):
            x = leftSnakeList[seg].rect.x + leftxChange
            y = leftSnakeList[seg].rect.y + leftyChange
            leftSnake = LeftSnake(x, y)
            leftSnakeList.insert(0, leftSnake)
            allSpritesList.add(leftSnake)
            leftSnakeList.remove(leftSnakeList[seg])
            allSpritesList.remove(leftSnakeList[seg])
            
        leftSnakeList.remove(leftSnakeList[-1])
        allSpritesList.remove(leftSnakeList[-1])

    else:
        x = leftSnakeList[0].rect.x + leftxChange
        y = leftSnakeList[0].rect.y + leftyChange
        leftSnakeList.remove(leftSnake)
        allSpritesList.remove(leftSnake)
        leftSnake = LeftSnake(x, y)
        leftSnakeList.insert(0, leftSnake)
        allSpritesList.add(leftSnake)
        
    '''leftSnakeList.remove(leftSnake)
    allSpritesList.remove(leftSnake)
    leftSnake = LeftSnake(x, y)
    leftSnakeList.insert(0, leftSnake)
    allSpritesList.add(leftSnake)'''

    # Make right snake move-----------------------------
    hitList = pygame.sprite.spritecollide(rightSnake, wallList, False)
    for block in hitList:
        pygame.quit()
        
    if len(rightSnakeList) > 1:
        oldSegment = rightSnakeList.pop()
        allSpritesList.remove(oldSegment)
        
    x = rightSnakeList[0].rect.x + rightxChange
    y = rightSnakeList[0].rect.y + rightyChange
    rightSnakeList.remove(rightSnake)
    allSpritesList.remove(rightSnake)
    rightSnake = RightSnake(x, y)
    rightSnakeList.insert(0, rightSnake)
    allSpritesList.add(rightSnake)
    # ---------------------------------------------------------------------

    # ----------------------Adding length----------------------------------
    # Left Snake--------------------------
    leftRedHits = pygame.sprite.spritecollide(leftSnake, leftRedList, True)
    for block in leftRedHits:
        x = leftSnakeList[0].rect.x + (20 * xNew)
        y = leftSnakeList[0].rect.y + (20 * yNew)
        leftAdd = LeftSnake(x, y)
        leftSnakeList.append(leftAdd)
        allSpritesList.add(leftAdd)
        totalLeftReds += 1
        leftRedx = random.randint(20, 760)
        while leftRedx % 20 != 0:
            leftRedx = random.randint(20, 760)
        leftRedy = random.randint(20, 760)
        while leftRedy % 20 != 0:
            leftRedy = random.randint(20, 760)
        leftRed = LeftRedBLock(leftRedx, leftRedy)
        allSpritesList.add(leftRed)
        leftRedList.add(leftRed)

    # Right Snake--------------------------
    rightRedHits = pygame.sprite.spritecollide(rightSnake, rightRedList, True)
    for block in rightRedHits:
        totalRightReds += 1
        rightRedx = random.randint(820, 1560)
        while rightRedx % 20 != 0:
            rightRedx = random.randint(820, 1560)
        rightRedy = random.randint(20, 760)
        while rightRedy % 20 != 0:
            rightRedy = random.randint(20, 760)
        rightRed = RightRedBLock(rightRedx, rightRedy)
        allSpritesList.add(rightRed)
        rightRedList.add(rightRed)

    # Splits the screen
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, [0, 0, 1600, 800])

    # Draw all sprites to screen
    allSpritesList.draw(screen)

    pygame.display.flip()
 
    clock.tick(10)

# Close the window and quit.
pygame.quit()
