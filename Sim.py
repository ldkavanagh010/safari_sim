__author__ = 'lkavanagh010'

import pygame
import sys
import os
from Map import Map
from Menu import GameMenu


class Sim:
    SCREENWIDTH = 800
    SCREENHEIGHT = 600
    SPRITE_SIZE = 16
    FLORA_COUNT = 0
    MAX_FLORA = 128
    FAUNA_COUNT = 0
    MAX_FAUNA = 32
    NUM_ITERATIONS = 100
    NUM_GENERATIONS = 0
    MAPWIDTH = 80
    MAPHEIGHT = 48
    FRAMERATE = 30

# INITIALIZATION FUNCTIONS
# Sim - __init__() and helper functions
# ------------------------------------------------------------------

    def __init__(self):

        #self-explanatory
        self.initialize_pygame()

        #create menu
        self.initialize_main_menu()

        #create screen
        self.initialize_screen()

        # draw  onto screen
        self.draw_start_screen()
        # begin main loop
        self.loop()

    def initialize_pygame(self):
        pygame.init()

        #create clock to track FPS
        self.clock = pygame.time.Clock()

    def initialize_main_menu(self):
        self.menu = GameMenu(self)

    def initialize_screen(self):
        #initialize screen with size
        self.width = self.SCREENWIDTH
        self.height = self.SCREENHEIGHT
        self.screen = pygame.display.set_mode((self.width, self.height))

        #create pygame surface for screen
        self.background = pygame.Surface(self.screen.get_size())


    def initialize_map(self):
        # initialize game map and game camera
        self.map = Map(self.MAPWIDTH, self.MAPHEIGHT, self)

        # create empty sprite groups for foreground objects
        self.plants = pygame.sprite.Group()
        self.animals = pygame.sprite.Group()


# ------------------------------------------------------------------------------


# DRAWING FUNCTIONS
# render program and rendering helper functions
# --------------------------------------------------------------------------------------

    def draw_start_screen(self):
        # clear screen
        self.background.fill((0,0,0))

        #load start image
        self.background = pygame.image.load(os.path.join('images', "start.png"))
        self.background = pygame.transform.scale(self.background, (self.SCREENWIDTH, self.SCREENHEIGHT))

        self.screen.blit(self.background, (0, 0))
        #display screen
        pygame.display.flip()



# -------------------------------------------------------------------------------------------



    def loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.menu.main_loop()


if __name__ == '__main__':
    simulator = Sim()



