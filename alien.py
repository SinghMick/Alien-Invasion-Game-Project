import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""
    
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen 
        
    # Load the alien imager and set its attributes
        self.image = pygame.image.load('Images/alien.bmp')
        self.rect = self.image.get_rect()

    #Start each alien near the top left corner of the screen 
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
    # Store the alien's exact horizontal position 
        self.x = float(self.rect.x)
    
    