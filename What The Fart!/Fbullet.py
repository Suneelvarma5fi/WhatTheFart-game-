############--REQUIREMENTS--##############
import pygame
from Butts import Butt
from gsettings import Settings
from pygame.sprite import Sprite
##########################################

class Bullet(Sprite):
    def __init__(self,screen):
        '''a fart object at butts current position'''
        super().__init__()
        #ready state
        self.screen = screen
        self.butt = Butt(screen)
        self.settings = Settings()
        self.bullet = pygame.image.load('Img/fart2.png')
        self.rect = self.bullet.get_rect()
        self.rect.bottom = self.butt.rect.top
        #self.bullet_state = 'ready'
        
        #for sprites
        self.x = self.rect.x
    
    #LIFE CYCLE OF FART
    # ready -> FART is about to be created
    # fire -> just fired it's moving
    
    def blitbullet(self):
        
        if self.rect.bottom <= 0:
            #self.bullet_state = 'ready'
            self.rect.bottom = self.butt.rect.top
        else:
            self.rect.bottom -= self.settings.bullet_speed
            self.screen.blit(self.bullet,self.rect)
            
    def update(self,x):
#        if x:
#            self.rect.right = x-20
#        #adjusting the bullet from the right position
#            self.blitbullet()
#        
#        #elif self.bullet_state == 'fire':
#        else:
        self.rect.right = self.rect.right
        self.blitbullet()