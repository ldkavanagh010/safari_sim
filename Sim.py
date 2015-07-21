__author__ = 'lkavanagh010'

import pygame
from Map import Map, Camera
from Tiles import Grass, Water
from Flora import Flora
import sys

class Sim:
    SCREENWIDTH = 800
    SCREENHEIGHT = 600
    SPRITE_SIZE = 16
    FLORA_COUNT = 0
    MAX_FLORA = 64
    NUM_ITERATIONS = 1000
    NUM_GENERATIONS = 64
    MAPWIDTH = 80
    MAPHEIGHT = 48
    FRAMERATE = 30

    def __init__(self):

        self.initialize_pygame()

        #map to sprite conversion
        self.initialize_map()

        # draw map onto screen
        self.draw()

        self.loop()



    def loop(self):
        while True:
            for event in pygame.event.get():
                # allow for quitting
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # control keyboard events
                if event.type == pygame.KEYDOWN:
                    if pygame.key.get_pressed()[pygame.K_DOWN]:
                        self.camera.cam_y += 5
                    if pygame.key.get_pressed()[pygame.K_UP]:
                        self.camera.cam_y -= 5
                    if pygame.key.get_pressed()[pygame.K_LEFT]:
                        self.camera.cam_x -= 5
                    if pygame.key.get_pressed()[pygame.K_RIGHT]:
                        self.camera.cam_x += 5


                self.tick()
                self.draw()
                # limit FPS and print to console
                self.clock.tick(self.FRAMERATE)
                print("FPS:" + self.clock.get_fps().__str__())


    def initialize_map(self):
        # initialize game map and game camera

        self.map = Map(self.MAPWIDTH, self.MAPHEIGHT)
        self.camera = Camera((self.MAPWIDTH / 2), (self.MAPHEIGHT/2))

        # create sprite group for background - terrain
        self.tiles = pygame.sprite.Group()
        x_offset = 0
        y_offset = 0
        for rows in self.map.Tiles:
            for entry in rows:

                entry.rect = entry.image.get_rect()
                entry.rect.topleft = (x_offset * 16, y_offset * 16)

                x_offset += 1

                self.tiles.add(entry)
            y_offset += 1
            x_offset = 0

        # create empty sprite groups for foreground objects
        self.plants = pygame.sprite.Group()
        self.animals = pygame.sprite.Group()
        #create pygame surface for screen
        self.background = pygame.Surface(self.screen.get_size())



    def tick(self):

        self.generate_flora()



    def draw(self):
        # clear screen
        self.background.fill((0,0,0))

        #camera logic
        self.draw_map()

        self.draw_plants()


        self.draw_animals()

        self.screen.blit(self.background, (0, 0))
        #display screen
        pygame.display.flip()


    def draw_map(self):
        for y in range(self.MAPHEIGHT):
            for x in range(self.MAPWIDTH):
                tile_x = (x * self.SPRITE_SIZE) - self.camera.cam_x
                tile_y = (y * self.SPRITE_SIZE) - self.camera.cam_y
                if self.onscreen(tile_x, tile_y):
                    self.map.Tiles[y][x].rect.topleft = (tile_x, tile_y)

        self.tiles.draw(self.background)


    def draw_plants(self):
        for plant in self.plants:
            tile_x = (plant.x_pos * self.SPRITE_SIZE) - self.camera.cam_x
            tile_y = (plant.y_pos * self.SPRITE_SIZE) - self.camera.cam_y
            if self.onscreen(tile_x, tile_y):
                plant.rect.topleft = (tile_x, tile_y)

        self.plants.draw(self.background)

    def draw_animals(self):
        pass

    def onscreen(self, x, y):
        return not (x < self.SPRITE_SIZE or x > self.SCREENWIDTH) or\
               (y < self.SPRITE_SIZE or y > self.SCREENHEIGHT)

    def generate_flora(self):
        while self.FLORA_COUNT <= self.MAX_FLORA:
            f = Flora()
            if self.valid_flora(f):
                f.rect = f.image.get_rect()
                f.rect.topleft = (f.x_pos * 16, f.y_pos * 16)
                self.plants.add(f)
                self.FLORA_COUNT += 1


    def valid_flora(self, flora):
        if self.map.Tiles[flora.y_pos][flora.x_pos].__str__() == 'GRASS'\
        and self.map.Tiles[flora.y_pos][flora.x_pos].is_occupied == False:
            return True
        else:
            return False

    def initialize_pygame(self):
        pygame.init()
        #initialize screen with size
        self.width = self.SCREENWIDTH
        self.height = self.SCREENHEIGHT
        self.screen = pygame.display.set_mode((self.width, self.height))

        #create clock to track FPS
        self.clock = pygame.time.Clock()




if __name__ == '__main__':
    simulator = Sim()



