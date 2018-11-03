import pygame 
import sys 

class Main: 
    
    # set up window
    size = (1000, 1000)
    screen = pygame.display.set_mode(size)
    BLACK = [0, 0, 0]
    screen.fill(BLACK)
    pygame.display.set_caption("Asteroids")
    
    earth_img = pygame.image.load('C:\Users\\bosil\Documents\Personal\PythonProjects3\phys_hacks\images\earth.png').convert_alpha()
    
    pygame.init() 

    # main program loop 
    done = False 
    while not done: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True 
                sys.exit() 
        
        
        screen.blit(earth_img, [200, 200])
        pygame.display.flip()
        
Main()