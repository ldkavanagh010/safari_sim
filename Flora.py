__author__ = 'lkavanagh010'

from Sprite import Sprite
import pygame, random


class Flora(Sprite):

    def __init__(self, map):
        super(Flora, self).__init__('flora.png')
        self.map = map
        self.rect = self.image.get_rect()


        self.x_pos = random.randint(0, self.map.MAPWIDTH - 1)
        self.y_pos = random.randint(0, self.map.MAPHEIGHT - 1)


    def valid_flora(self):
        if self.map.Tiles[self.y_pos][self.x_pos].__str__() == 'GRASS'\
        and self.map.Tiles[self.y_pos][self.x_pos].is_occupied == False:
            self.map.Tiles[self.y_pos][self.x_pos].is_occupied = True
            return True
        else:
            return False