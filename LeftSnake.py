# Left Snake
# Eric Olenski
# 4-12-16

import pygame

YELLOW = (255, 255, 0)
snakeWidth = 18
snakeHeight = 18

class LeftSnake(pygame.sprite.Sprite):
    
    """ Class to represent one segment of the snake. """
    
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([snakeWidth, snakeHeight])
        self.image.fill(YELLOW)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
