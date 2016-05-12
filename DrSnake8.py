# Dr. Snake 8
# Eric Olenski
# 4-28-16
 
import pygame
import random
from Walls import Wall
from LeftSnake import LeftSnake
from RightSnake import RightSnake
from LeftRedBLocks import LeftRedBLock
from RightRedBlock import RightRedBLock
from LeftBlueBlock import LeftBlueBlock
from RightBlueBlock import RightBlueBlock
 
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
screenHeight = 850
screenWidth = 1600
size = (screenWidth, screenHeight)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Dr. Snake")
allSpritesList = pygame.sprite.Group()
hitList = pygame.sprite.Group()
leftBlueList = pygame.sprite.Group()
rightBlueList = pygame.sprite.Group()

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
leftHit = pygame.sprite.Group()
leftSnake = LeftSnake(40, 40)
leftSnakeList.insert(0, leftSnake)
allSpritesList.add(leftSnake)
leftLoss = 0
# Right--------------------------------
rightSnakeList = []
rightHit = pygame.sprite.Group()
rightSnake = RightSnake(840, 40)
rightSnakeList.insert(0, rightSnake)
allSpritesList.add(rightSnake)
rightLoss = 0 
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
totalRightReds = 0
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
            if len(leftSnakeList) > 1:
                if leftxChange != 0 or leftyChange != 0:
                    if leftxChange < 0:
                        if event.key == pygame.K_a:
                            leftxChange = (snakeWidth + margin) * -1
                            leftyChange = 0

                        elif event.key == pygame.K_w:
                            leftxChange = 0
                            leftyChange = (snakeWidth + margin) * -1
                
                        elif event.key == pygame.K_s:
                            leftxChange = 0
                            leftyChange = (snakeWidth + margin)

                    elif leftxChange > 0:
                        if event.key == pygame.K_d:
                            leftxChange = (snakeWidth + margin)
                            leftyChange = 0

                        elif event.key == pygame.K_w:
                            leftxChange = 0
                            leftyChange = (snakeWidth + margin) * -1
                
                        elif event.key == pygame.K_s:
                            leftxChange = 0
                            leftyChange = (snakeWidth + margin)
                    
                    elif leftyChange < 0:
                        if event.key == pygame.K_w:
                            leftxChange = 0
                            leftyChange = (snakeWidth + margin) * -1

                        elif event.key == pygame.K_a:
                            leftxChange = (snakeWidth + margin) * -1
                            leftyChange = 0

                        elif event.key == pygame.K_d:
                            leftxChange = (snakeWidth + margin)
                            leftyChange = 0

                    else:
                        if event.key == pygame.K_s:
                            leftxChange = 0
                            leftyChange = (snakeWidth + margin)

                        elif event.key == pygame.K_a:
                            leftxChange = (snakeWidth + margin) * -1
                            leftyChange = 0

                        elif event.key == pygame.K_d:
                            leftxChange = (snakeWidth + margin)
                            leftyChange = 0

            else:
                if event.key == pygame.K_a:
                    leftxChange = (snakeWidth + margin) * -1
                    leftyChange = 0

                elif event.key == pygame.K_d:
                    leftxChange = (snakeWidth + margin)
                    leftyChange = 0
                
                elif event.key == pygame.K_w:
                    leftxChange = 0
                    leftyChange = (snakeWidth + margin) * -1
                
                elif event.key == pygame.K_s:
                    leftxChange = 0
                    leftyChange = (snakeWidth + margin)

        # Set right snake direction---------------------
            if len(rightSnakeList) > 1:
                if rightxChange != 0 or rightyChange != 0:
                    if rightxChange < 0:
                        if event.key == pygame.K_LEFT:
                            rightxChange = (snakeWidth + margin) * -1
                            rightyChange = 0

                        elif event.key == pygame.K_UP:
                            rightxChange = 0
                            rightyChange = (snakeWidth + margin) * -1
                
                        elif event.key == pygame.K_DOWN:
                            rightxChange = 0
                            rightyChange = (snakeWidth + margin)

                    elif rightxChange > 0:
                        if event.key == pygame.K_RIGHT:
                            rightxChange = (snakeWidth + margin)
                            rightyChange = 0

                        elif event.key == pygame.K_UP:
                            rightxChange = 0
                            rightyChange = (snakeWidth + margin) * -1
                
                        elif event.key == pygame.K_DOWN:
                            rightxChange = 0
                            rightyChange = (snakeWidth + margin)
                    
                    elif rightyChange < 0:
                        if event.key == pygame.K_UP:
                            rightxChange = 0
                            rightyChange = (snakeWidth + margin) * -1

                        elif event.key == pygame.K_LEFT:
                            rightxChange = (snakeWidth + margin) * -1
                            rightyChange = 0
    
                        elif event.key == pygame.K_RIGHT:
                            rightxChange = (snakeWidth + margin)
                            rightyChange = 0

                    else:
                        if event.key == pygame.K_DOWN:
                            rightxChange = 0
                            rightyChange = (snakeWidth + margin)

                        elif event.key == pygame.K_LEFT:
                            rightxChange = (snakeWidth + margin) * -1
                            rightyChange = 0

                        elif event.key == pygame.K_RIGHT:
                            rightxChange = (snakeWidth + margin)
                            rightyChange = 0
                        
            else:
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
        leftxChange = 0
        leftyChange = 0
        font = pygame.font.SysFont('Calibri', 100, True, False)
        lText = font.render("Get Better", True, BLUE)
        leftLoss = 1
        
    if len(leftSnakeList) > 1:
        oldSegment = leftSnakeList.pop()
        allSpritesList.remove(oldSegment)
        x = leftSnakeList[0].rect.x + leftxChange
        y = leftSnakeList[0].rect.y + leftyChange
        leftSnake = LeftSnake(x, y)
        leftSnakeList.insert(0, leftSnake)
        allSpritesList.add(leftSnake)
    
    else:
        x = leftSnakeList[0].rect.x + leftxChange
        y = leftSnakeList[0].rect.y + leftyChange
        leftSnakeList.remove(leftSnake)
        allSpritesList.remove(leftSnake)
        leftSnake = LeftSnake(x, y)
        leftSnakeList.insert(0, leftSnake)
        allSpritesList.add(leftSnake)

    # Make right snake move-----------------------------
    hitList = pygame.sprite.spritecollide(rightSnake, wallList, False)
    for block in hitList:
        rightxChange = 0
        rightyChange = 0
        rfont = pygame.font.SysFont('Calibri', 100, True, False)
        rText = rfont.render("Get Better", True, BLUE)
        rightLoss = 1
        
    if len(rightSnakeList) > 1:
        oldSegment = rightSnakeList.pop()
        allSpritesList.remove(oldSegment)
        x = rightSnakeList[0].rect.x + rightxChange
        y = rightSnakeList[0].rect.y + rightyChange
        rightSnake = RightSnake(x, y)
        rightSnakeList.insert(0, rightSnake)
        allSpritesList.add(rightSnake)
        
    else:
        x = rightSnakeList[0].rect.x + rightxChange
        y = rightSnakeList[0].rect.y + rightyChange
        rightSnakeList.remove(rightSnake)
        allSpritesList.remove(rightSnake)
        rightSnake = RightSnake(x, y)
        rightSnakeList.insert(0, rightSnake)
        allSpritesList.add(rightSnake)
    # ---------------------------------------------------------------------

    # ------------------Make sure you can't run into your own snake--------
    # Left snake---------------------------
    leftCheck = pygame.sprite.Group()
    for thing in leftSnakeList[1:]:
        leftCheck.add(thing)
    if leftRedHits == False:
        leftHit = pygame.sprite.spritecollide(leftSnake, leftCheck, True)
        for block in leftHit:
            leftxChange = 0
            leftyChange = 0
            font = pygame.font.SysFont('Calibri', 100, True, False)
            lText = font.render("Get Better", True, BLUE)
            leftLoss = 1

    # Right snake--------------------------
    rightCheck = pygame.sprite.Group()
    for thing in rightSnakeList[1:]:
        rightCheck.add(thing)
    if rightRedHits == False:
        rightHit = pygame.sprite.spritecollide(rightSnake, rightCheck, True)
        for block in rightHit:
            rightxChange = 0
            rightyChange = 0
            rfont = pygame.font.SysFont('Calibri', 100, True, False)
            rText = rfont.render("Get Better", True, BLUE)
            rightLoss = 1

    # ----------------------Adding length----------------------------------
    # Left Snake--------------------------
    leftRedHits = pygame.sprite.spritecollide(leftSnake, leftRedList, True)
    for block in leftRedHits:
        for i in range(5):
            x = leftSnakeList[0].rect.x 
            y = leftSnakeList[0].rect.y 
            leftAdd = LeftSnake(x, y)
            leftSnakeList.append(leftAdd)
            allSpritesList.add(leftAdd)
        leftRedx = random.randint(20, 760)
        while leftRedx % 20 != 0:
            leftRedx = random.randint(20, 760)
        leftRedy = random.randint(20, 760)
        while leftRedy % 20 != 0:
            if totalLeftReds > 20:
                allSpritesList.remove(leftBlue)
            leftRedy = random.randint(20, 760)
        leftRed = LeftRedBLock(leftRedx, leftRedy)
        allSpritesList.add(leftRed)
        leftRedList.add(leftRed)
        totalLeftReds += 1
        if totalLeftReds % 20 == 0:
            leftBlueList = pygame.sprite.Group()
            leftBluex = random.randint(20, 760)
            while leftBluex % 20 != 0:
                leftBluex = random.randint(20, 760)
            leftBluey = random.randint(20, 760)
            while leftBluey % 20 != 0:
                leftBluey = random.randint(20, 760)
            leftBlue = LeftBlueBlock(leftBluex, leftBluey)
            leftBlueList.add(leftBlue)
            allSpritesList.add(leftBlue)
    leftRedHits = False

    # Right Snake--------------------------
    rightRedHits = pygame.sprite.spritecollide(rightSnake, rightRedList, True)
    for block in rightRedHits:
        for i in range(5):
            x = rightSnakeList[0].rect.x 
            y = rightSnakeList[0].rect.y 
            rightAdd = RightSnake(x, y)
            rightSnakeList.append(rightAdd)
            allSpritesList.add(rightAdd)
        rightRedx = random.randint(820, 1560)
        while rightRedx % 20 != 0:
            rightRedx = random.randint(820, 1560)
        rightRedy = random.randint(20, 760)
        while rightRedy % 20 != 0:
            rightRedy = random.randint(20, 760)
        rightRed = RightRedBLock(rightRedx, rightRedy)
        allSpritesList.add(rightRed)
        rightRedList.add(rightRed)
        totalRightReds += 1
        if totalRightReds % 20 == 0:
            if totalRightReds > 20:
                allSpritesList.remove(rightBlue)
            rightBlueList = pygame.sprite.Group()
            rightBluex = random.randint(820, 1560)
            while rightBluex % 20 != 0:
                rightBluex = random.randint(820, 1560)
            rightBluey = random.randint(20, 760)
            while rightBluey % 20 != 0:
                rightBluey = random.randint(20, 760)
            rightBlue = RightBlueBlock(rightBluex, rightBluey)
            rightBlueList.add(rightBlue)
            allSpritesList.add(rightBlue)
    rightRedHits = False
    # ---------------------------------------------------------------------

    # ------------------Taking length away power up(Blue blocks)-----------
    # Left --------------------------------
    leftBlueHits = pygame.sprite.spritecollide(leftSnake, leftBlueList, True)
    for block in leftBlueHits:
        oldLength = len(rightSnakeList)
        allSpritesList.remove(rightSnakeList)
        rightSnakeList = []
        rightSnakeList.append(rightSnake)
        for seg in range(oldLength - 51):
            x = rightSnakeList[0].rect.x 
            y = rightSnakeList[0].rect.y 
            rightAdd = RightSnake(x, y)
            rightSnakeList.append(rightAdd)
            allSpritesList.add(rightAdd)
        leftBlueList.remove(leftBlue)

    # Right --------------------------------
    rightBlueHits = pygame.sprite.spritecollide(rightSnake, rightBlueList, True)
    for block in rightBlueHits:
        oldLength = len(leftSnakeList)
        allSpritesList.remove(leftSnakeList)
        leftSnakeList = []
        leftSnakeList.append(leftSnake)
        for seg in range(oldLength - 51):
            x = leftSnakeList[0].rect.x 
            y = leftSnakeList[0].rect.y 
            leftAdd = LeftSnake(x, y)
            leftSnakeList.append(leftAdd)
            allSpritesList.add(leftAdd)
        rightBlueList.remove(rightBlue)
    # ---------------------------------------------------------------------
    
    # Splits the screen
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, [0, 0, 1600, 800])

    # Draw all sprites to screen
    allSpritesList.draw(screen)

    # Display scores
    # Left Snake
    font = pygame.font.SysFont('Calibri', 40, True, False)
    text = font.render("Length: " + str(len(leftSnakeList)), True, BLUE)
    screen.blit(text, [0, 800])

    # Right Snake
    font = pygame.font.SysFont('Calibri', 40, True, False)
    text = font.render("Length: " + str(len(rightSnakeList)), True, BLUE)
    screen.blit(text, [800, 800])

    # Loss Message
    if leftLoss > 0:
        screen.blit(lText, [200, 200])

    if rightLoss > 0:
        screen.blit(rText, [1000, 200])
        
    pygame.display.flip()
 
    clock.tick(12)

# Close the window and quit.
pygame.quit()

