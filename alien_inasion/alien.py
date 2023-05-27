import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    
    #A class to represent a single alien in the flet
    def __init__ (self,ai_settings,screen):
        #initialize the alien and its starting position
        super(Alien,self).__init__()
        self.screen=screen
        self.ai_settings = ai_settings
        
        #load the alien image and st its rect attribute
        self.image = pygame.image.load('ajlien.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()


        #start each new alien near the op of the screen
        self.rect.x = self.rect.width
        self.rect.left = self.screen_rect.left

        #store alien's exact position
        self.x=float(self.rect.x)

    def blitime(self):
        #draw the alien at its current location
        self.screen.blit(self.image,self.rect)

