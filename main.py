# Example file showing a basic pygame "game loop"
import pygame
from gamerpg import Gamerpg
# pygame setup
pygame.init()
running = True
game = Gamerpg()
while running:
    
    
    if (game.run()) == False:
        running = False

pygame.quit()