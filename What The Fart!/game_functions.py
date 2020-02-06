import sys
import pygame
from Noses import Nose
import random
from Fbullet import Bullet

'''###############################KEY--EVENTS##################################'''

def when_keydown(butts,bullets,event,screen):
    '''when key pressed'''
    if event.key == pygame.K_RIGHT:
        #if right moving right will be true.updated in butts module
        butts.moving_right = True
        butts.moving_left = False

    elif event.key == pygame.K_LEFT:
        #if left moving left will be updated in butts module
        butts.moving_left = True
        butts.moving_right = False
        
    elif event.key == pygame.K_UP:
        if len(bullets) <= 1:
            
            new_bullet = Bullet(screen)
            new_bullet.rect.right = butts.bullet_pos-20
            bullets.add(new_bullet)
            butts.play_sound()
            #return butts.bullet_pos
        
        
#        if bullet.bullet_state == 'ready':
#            bullet.bullet_state = 'fire'
#            return butts.bullet_pos
        
    elif event.key == pygame.K_q:
        pygame.quit()
        sys.exit()
        
        
def when_keyup(butts,event):
    '''when key released'''
    if event.key == pygame.K_RIGHT:
        #if right moving right will be true.updated in butts module
        butts.moving_right = False

    elif event.key == pygame.K_LEFT:
        #if left moving left will be updated in butts module
        butts.moving_left = False
    

def check_events(butts,bullets,screen):
    '''a functions to check events'''
    #Setting keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            #when key is pressed it may be either right or left
            when_keydown(butts,bullets,event,screen)
            #return x
            
        elif event.type == pygame.KEYUP:
            #when key is released the movement will be set to false
            #update method in butts module won't work
            when_keyup(butts,event)
            
'''###############################KEY-EVENTS###################################'''
      
            
'''############################--NOSES BEGIN--#################################'''
  
def update_noses(noses):
    """update positions of all noses"""
    noses.update()
             
 
def random_noses(space,screen,noses):
    '''creating noses one by one'''
    
    for each_nose in space:
        nose = Nose(screen)
        nose.rect.x = random.randint(each_nose[0],each_nose[1])
        noses.add(nose)          
            
def create_fleet(settings,screen,noses):
    '''create a full fleet of noses'''
    
    tot_noses = random.randint(2,5)
    #creating a row full of noses
    
    if tot_noses == 5:
        space = [(100,160),(200,340),(380,520),(560,700),(740,900)]
        random_noses(space,screen,noses)
        
    elif tot_noses == 4:
        space = [(100,280),(320,480),(520,680),(720,900)]
        random_noses(space,screen,noses)
        
    elif tot_noses == 3:
        space = [(100,280),(320,580),(620,900)]
        random_noses(space,screen,noses)
        
    elif tot_noses == 2:
        space = [(100,480),(520,900)]
        random_noses(space,screen,noses)
        
'''##################################--END-NOSES--###############################'''

'''################################-COLLISIONS-################################'''
            
def check_collisions(bullets,noses,settings,screen):
    """make noses and bullets disappear after collision"""
    pygame.sprite.groupcollide(bullets,noses,True,True)
    
    
    
    if len(noses) in (0,1,2):
        create_fleet(settings,screen,noses)
        

'''################################-COLLISIONS-################################'''
            
'''#################################BULLET FART##############################'''

def rm_oldbullet(bullets):
    '''removing old bulllets from the group'''
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            
def bullet_update(butts,bullets,x):
    '''updating each bullet in the GROUP'''
    for bullet in bullets.sprites():
        bullet.update(x)
    
'''##############################FART END######################################'''     

'''#############################RANDOM-CHICKEN#################################'''

        
'''#############################RANDOM-CHICKEN#################################'''
  
'''###########################SCREEN UPDATION##################################'''
      
def update_surface(settings,butts,bullets,noses,x,screen):
    '''updating the screen while every loop'''
    screen.fill(settings.bg_color)
    #updating filling the surface color
    butts.blitme()
    #updating the position of image on surface
    bullet_update(butts,bullets,x)
    #displaying the bullet when key_up pressed
    noses.draw(screen)
    #displaying group of noses on the screen
    
    pygame.display.flip()
    #Updating the display image
    
'''############################################################################'''