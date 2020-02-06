import pygame
from gsettings import Settings
from pygame.sprite import Sprite

class Nose(Sprite):
    '''A nose object for enemy role'''
    def __init__(self,screen):
        super().__init__()
        self.settings = Settings()
        self.screen = screen
        self.image = pygame.image.load("Img/nose2.png")
        self.rect = self.image.get_rect()
        self.rect.bottom = float(90.0)
        # Start each new nose near the top left of the screen
        self.rect.top = -100
        #Store the nose's exact position
        self.x = float(self.rect.x)
        #nose movement parameters
        self.nose_moving_left = False
        self.nose_moving_right = True
    
        
    def nose_moving_rightside(self):
        '''nose moving right side when True'''
       
        if self.rect.right >= 990:
            self.rect.bottom += self.rect.height
            self.nose_moving_right = False
            self.nose_moving_left = True
            
        elif self.rect.right < 990:
            self.rect.centerx += 1
                
            
    def nose_moving_leftside(self):
        '''noses moving right when True'''
        if self.rect.left <= 10:
            self.rect.bottom += self.rect.height
            self.nose_moving_left = False
            self.nose_moving_right = True
                
        elif self.rect.left > 10:
            self.rect.left -= 1
        
    def update(self):
        """move all noses down"""
        if self.nose_moving_right:
            self.nose_moving_rightside()

        if self.nose_moving_left:
            self.nose_moving_leftside()
            
        
    def blitnose(self):
        '''Displaying nose on the screen'''
        self.screen.blit(self.image,self.rect)