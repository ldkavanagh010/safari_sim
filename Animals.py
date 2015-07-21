__author__ = 'lkavanagh010'
import pygame, random, os
from Sprite import Sprite
from Network import NeuralNetwork


class Animal(Sprite):



    def __init__(self, name):
        super(Animal, self).__init__(name)
        self.x_pos = random.randint(0, 79)
        self.y_pos = random.randint(0, 47)
        self.hunger = random.randint(0, 100)
        self.tiredness = random.randint(0, 100)
        self.rect = self.image.get_rect()

    def eat(self):
        pass
    def move(self):
        pass
    def sleep(self):
        pass
    def think(self):
        pass

class Gazelle(Animal):
    def __init__(self):
        super(Gazelle, self).__init__('gazelle.png')

class Lion(Animal):
    def __init__(self):
        super(Lion, self).__init__('lion.png')
