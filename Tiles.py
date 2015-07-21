__author__ = 'lkavanagh010'
import pygame
from Sprite import Sprite

class Tile(Sprite):
    def __init__(self, name):
        super(Sprite, self).__init__(name)
        self.rect = self.image.get_rect()


class Water(Sprite):
    def __init__(self):
        super(Water, self).__init__("water.png")


    def __str__(self):
        return "WATER"

class Grass(Sprite):
    def __init__(self):
        super(Grass, self).__init__("grass.png")
        self.is_occupied = False

    def __str__(self):
        return "GRASS"
