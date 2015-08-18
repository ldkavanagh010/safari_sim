__author__ = 'lkavanagh010'

import pygame
import os
from Map import Map

class GameMenu():

    def __init__(self, sim):
        self.sim = sim

        # start button for main menu
        self.startbutton = pygame.image.load(os.path.join('images', "startbutton.png"))
        self.sbrect = self.startbutton.get_rect()
        self.sbrect.topleft = (self.sim.SCREENWIDTH/2 - 100, self.sim.SCREENHEIGHT/2 - 150)

# Menu Functions
#-----------------------------------------------------------------------------------------


# Draw Functions
#--------------------------------------------------------------------------------------------

    def draw_main_menu(self):
        self.sim.background.fill((0, 0 ,0))


        self.sim.screen.blit(self.sim.background, (0, 0))
        self.sim.screen.blit(self.startbutton, self.sbrect.topleft)

        pygame.display.flip()

    def draw_options_screen(self):
        pass


# loops
#--------------------------------------------------------------------------------------------


    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN &\
                self.sbrect.collidepoint(pygame.mouse.get_pos()):
                    print("click")
                    self.sim.map = Map(self.sim.MAPWIDTH, self.sim.MAPHEIGHT, self.sim)

            self.draw_main_menu()

    def options_loop(self):
        pass

# ------------------------------------------------------------------------------------------
