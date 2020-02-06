import pygame
from gsettings import Settings
#from Fbullet import Bullet
from pygame.sprite import Sprite
class Butt(Sprite):
    '''In this class, We take the screen object as an argument and 
       according to the screen surface rect coordinates one must arrange
       the game elements(rects) using the surface_rect as reference'''
       
    def __init__(self,screen):
        super().__init__()
        #inorder to make these butts appear we need a screen
        #screen is passed as an argument
        self.screen = screen
        self.settings = Settings()
        #An instance for the surface created
        self.image = pygame.image.load('Img/butts.png')
        #Above line loads the images on the surface
        self.rect = self.image.get_rect()
        #Here, in pygame the game elements referred as rects
        #so, the loaded images is converted into an image rects
        self.screen_rect = screen.get_rect()
        #screen_rect is the surface rectangle
        
        #start at the bottom center of surface
        self.rect.centerx = float(self.screen_rect.centerx)
        '''imgrect.centerx'''
        #surface center(screen_rect.centerx) is stored in 
        self.rect.bottom = self.screen_rect.bottom
        '''imgrect.bottom'''
        #surface bottom(screen_rect.bottom) is stored in 
        
        #butt movement
        self.moving_right = False
        self.moving_left = False
        self.bullet_pos = self.rect.right
        #fart sound when farted
        self.fart_sound = pygame.mixer.Sound("sounds/fartsound2.wav")
        
    def play_sound(self):
        #play method
        self.fart_sound.play()
        
    def update(self):
        '''updating the location of butts in every while loop'''
        
        if self.moving_right and self.rect.right <= self.settings.screen_width:
            self.rect.centerx += self.settings.speed_control
                
        elif self.moving_left and self.rect.left >= 0:
            self.rect.centerx -= self.settings.speed_control
        #for bullet position 
        self.bullet_pos = self.rect.right
        
   
        
    def blitme(self):
        '''Drawing butts at its current location'''
        self.screen.blit(self.image,self.rect) 
   
     
    
            
        