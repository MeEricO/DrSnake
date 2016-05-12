# Left Blue Blocks
# Eric Olenski
# 4-28-16

import pygame

BLUE = (0, 0, 225)
snakeWidth = 18
snakeHeight = 18

class LeftBlueBlock(pygame.sprite.Sprite):
    
    """ Takes length away from your own snake. """
    
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([snakeWidth, snakeHeight])
        self.image.fill(BLUE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
