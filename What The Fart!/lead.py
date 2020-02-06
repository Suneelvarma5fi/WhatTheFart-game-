###############--REQUIREMENTS--##################
import pygame
from gsettings import Settings
from Butts import Butt
import game_functions as gf
#from Fbullet import Bullet
from pygame.sprite import Group
#################################################

    
def run_game():
    #initialize game & screen objectt
    pygame.init() #called the pygame init constructor
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))
    #set the background code
    #the screen object is called a surface
    #On that surface we'll keep our elements
    pygame.display.set_caption("What the Fart!")
    #Object creation of items on the screen
    butt = Butt(screen)
    #creating a group of noses using sprite.Group()
    noses = Group()
    #create a group of aliens
    bullets = Group()
    #creating group of bullets
    gf.create_fleet(settings,screen,noses)  
    while True:
        x = gf.check_events(butt,bullets,screen)
        #checks the events in for loop get_events()
        butt.update()
        #updating the butt positions
        gf.bullet_update(butt,bullets,x)  
        #creating and updating bullets
        gf.rm_oldbullet(bullets)
        #removing old bullets from the sprite group
        gf.update_noses(noses)
        #update noses and their movement
        gf.check_collisions(bullets,noses,settings,screen)
        #collision between noses and bullet farts
        gf.update_surface(settings,butt,bullets,noses,x,screen)
        #filling the color, updating the obj positions
        
        
if __name__ == '__main__':
    run_game()