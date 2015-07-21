__author__ = 'lkavanagh010'

import pygame, os

class Sprite(pygame.sprite.Sprite):

    def loadimage(self, name):
        image = pygame.image.load(os.path.join('images',name)).convert_alpha()
        return image

    def __init__(self, name):
        super(Sprite, self).__init__()
        self.image = self.loadimage(name)