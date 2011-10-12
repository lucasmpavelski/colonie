import pygame
from utils import *

class Ant (pygame.sprite.Sprite) :
    def __init__ (self) :
        pygame.sprite.Sprite.__init__(self)
        self.image = load_img("ant.png")
        self.rect = self.image.get_rect()

    def update (self) :
        pass
