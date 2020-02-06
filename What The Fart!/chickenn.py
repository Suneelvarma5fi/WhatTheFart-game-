import pygame
from pygame.sprite import Sprite
from random import randint

class Chicken(Sprite):
    def __init__(self,screen):
        self.screen = screen
        super().__init__()
        self.image = pygame.image.load("Img/chicken.png")
        self.rect = self.image.get_rect()
    
        
    def blitting_chicken1(self):
        self.rect.topright = (randint(50,500),randint(400,600))
        self.screen.blit(self.image,self.rect)
    def blitting_chicken2(self):
        self.rect.topright = (randint(600,950),randint(400,600))
        self.screen.blit(self.image,self.rect)