__author__ = 'lkavanagh010'

from Sprite import Sprite
import pygame, random


class Flora(Sprite):

    def __init__(self):
        super(Flora, self).__init__('flora.png')
        self.map = map
        self.rect = self.image.get_rect()


        self.x_pos = random.randint(0, 79)
        self.y_pos = random.randint(0, 47)


