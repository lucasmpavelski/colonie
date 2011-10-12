import pygame, sys
from pygame.locals import *

from ant import Ant

class Simulation :
    def __init__ (self):
        SIZE = (640, 400)
        BG_COLOUR = (255, 255, 255)

        init = pygame.init()
        self.screen = pygame.display.set_mode(SIZE)
        self.screen.fill(BG_COLOUR)

        a = Ant()
        self.allsprites = pygame.sprite.RenderPlain((a))

    def play (self):
        clock = pygame.time.Clock()
        running = True
        while running : 
            for event in pygame.event.get () :
                if event.type == QUIT : 
                    running = False
                    self.exit()
            self._redraw()
            clock.tick(20)
            
    def _redraw (self) :
        self.allsprites.update()
        self.screen.fill((255, 255, 255))
        self.allsprites.draw(self.screen)
        pygame.display.flip()
     
    def exit (self) :
        sys.exit()

if __name__ == "__main__" :
    s = Simulation()
    s.play()
