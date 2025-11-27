import pygame

class World:
    def __init__(self, game):
        
        self.game = game
        self.screen = game.screen
        self.tiles = [[1, 0, 0, 1, 1],
                      [1, 1, 0, 0, 1],
                      [0, 1, 1, 1, 0],
                      [1, 0, 0, 1, 1],
                      [1, 1, 0, 0, 1]]
    
    def load_level(self):
        for y in range(len(self.tiles)):
            for x in range(len(self.tiles[y])):
                #todo: load asset instead of drawing rectangles
                #--------------------------------------------------------------------------------
                tile = self.tiles[y][x]
                if tile == 1:
                    pygame.draw.rect(self.screen, "green", pygame.Rect(x*32, y*32, 32, 32))#change this to pygame image blit
                    ##self.screen.blit(pygame.image.load("assets/1.png"), (x*32, y*32))
                #--------------------------------------------------------------------------------
                
        
    def update(self):
        pass
            