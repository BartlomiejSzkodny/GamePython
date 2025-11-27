import pygame
from world import World
class Gamerpg:
    def __init__(self):
        self.screen = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock() 
        self.clock.tick(120)  # limits FPS to 60
        self.screen.fill("purple")
        # pass the game instance to World so World can access screen and other resources
        self.world = World(self)
    def run(self) -> bool:
        
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        
        self.world.load_level()
