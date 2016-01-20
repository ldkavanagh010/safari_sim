__author__ = 'lkavanagh010'

import pygame
import sys
import os
from Map import Map


class GameMenu():

    def __init__(self, sim):
        self.sim = sim

        # start button for main menu
        self.startbutton = pygame.image.load(os.path.join('images', "startbutton.png"))
        self.optionsbutton = pygame.image.load(os.path.join('images', "optionsbutton.png"))
        self.sbrect = self.startbutton.get_rect()
        self.sbrect.topleft = (self.sim.SCREENWIDTH/2 - 100, self.sim.SCREENHEIGHT/2 - 150)
        self.obrect = self.optionsbutton.get_rect()
        self.obrect.topleft = (self.sim.SCREENWIDTH/2 - 100, self.sim.SCREENHEIGHT/2 - 25)

# Menu Functions
#-----------------------------------------------------------------------------------------


# Draw Functions
#--------------------------------------------------------------------------------------------

    def draw_main_menu(self):
        self.sim.background.fill((0, 0 ,0))

        self.sim.screen.blit(self.sim.background, (0, 0))
        self.sim.screen.blit(self.startbutton, self.sbrect.topleft)
        self.sim.screen.blit(self.optionsbutton, self.obrect.topleft)

        pygame.display.flip()

    def draw_options_screen(self):
        pass


# loops
#--------------------------------------------------------------------------------------------


    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    print("click")
                    if self.sbrect.collidepoint(x, y):
                        self.sim.map = Map(self.sim.MAPWIDTH, self.sim.MAPHEIGHT, self.sim)
                    if self.obrect.collidepoint(x, y):
                        self.options = Options(self.sim)

            self.draw_main_menu()

# ------------------------------------------------------------------------------------------

class Options():

    def __init__(self, sim):
        self.sim = sim

        self.options_loop()


    def draw_options(self):
        self.sim.background.fill((0, 0 ,0))
        self.sim.screen.blit(self.sim.background, (0, 0))
        pygame.display.flip()


    def options_loop(self):
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                   pass

            self.draw_options()