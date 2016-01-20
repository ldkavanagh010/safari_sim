import sys

__author__ = 'lkavanagh010'
import pygame
import random
from Tiles import Grass, Water
from Flora import Flora
from Fauna import Gazelle


class Map():

    HEIGHTS = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Map Constructor & Constructor Helper Functions
#---------------------------------------------------------------------------------------------------------------------
    def __init__(self, width, height, sim):
        self.sim = sim
        self.MAPWIDTH = width
        self.MAPHEIGHT = height

        self.plants = pygame.sprite.Group()
        self.animals = pygame.sprite.Group()


        self.camera = Camera((self.MAPWIDTH / 2), (self.MAPHEIGHT/2))

        self.generate_tiles()
        # create sprite group for background - terrain
        self.tiles_to_sprites()

        self.generate_flora()

        self.generate_animals()

        self.loop()


# create randomly assigned heightmap of map-size.
# turn heightmap into game tiles
    def generate_tiles(self):
        self.heightmap=[]
        self.Tiles=[]
        q=[]
        for h in range(self.MAPHEIGHT):
            for w in range(self.MAPWIDTH): q.append(random.choice(self.HEIGHTS))
            self.heightmap.append(q)
            q=[]
        for w in range(self.MAPHEIGHT):
            for h in range(self.MAPWIDTH): q.append('')
            self.Tiles.append(q)
            q=[]

        r_i = 0 # index of row
        for h_row in self.heightmap:
            c_i = 0 # index of column
            for height in h_row:
                is_grass = self.chance_of_grass(height) >= random.randint(1, 100)
                self.Tiles[r_i][c_i] = Grass() if is_grass else Water()
                c_i += 1
            r_i += 1

# determine the % chance of a tile being water or grass based on tile-height.
    def chance_of_grass(self, height):
        if   height == 0: return 100
        elif height <= 3: return 100
        elif height <= 4: return 100
        elif height <= 7: return 100

        return 100

# place tiles in pygame sprite group with appropriate coordinate placement.
    def tiles_to_sprites(self):
        self.bg_sprites = pygame.sprite.Group()
        x_offset = 0
        y_offset = 0
        for rows in self.Tiles:
            for entry in rows:

                entry.rect = entry.image.get_rect()
                entry.rect.topleft = (x_offset * 16, y_offset * 16)

                x_offset += 1

                self.bg_sprites.add(entry)
            y_offset += 1
            x_offset = 0


# Map World Functions & Helpers
#----------------------------------------------------------------------------------


    def map_tick(self):
        self.generate_flora()

        for animal in self.animals:
            animal.think()



    def generate_flora(self):
        while self.sim.FLORA_COUNT <= self.sim.MAX_FLORA:
            f = Flora(self)
            if f.valid_flora():
                f.rect = f.image.get_rect()
                f.rect.topleft = (f.x_pos * 16, f.y_pos * 16)
                self.plants.add(f)
                self.sim.FLORA_COUNT += 1


    def generate_animals(self):
        while self.sim.FAUNA_COUNT <= self.sim.MAX_FAUNA:
            a = Gazelle(self)
            if a.valid_fauna():
                a.rect = a.image.get_rect()
                a.rect.topleft = (a.x_pos * 16, a.y_pos * 16)
                self.animals.add(a)
                self.sim.FAUNA_COUNT += 1



#---------------------------------------------------------------------------------

# Draw functions & Draw Helpers
#-------------------------------------------------------------------------------------------------------------------

    def draw_map(self):

        self.sim.background.fill((0, 0, 0))

        self.draw_bg()

        self.draw_plants()

        self.draw_animals()

        self.sim.screen.blit(self.sim.background, (0, 0))

        pygame.display.flip()

    def draw_bg(self):
        for y in range(self.MAPHEIGHT):
            for x in range(self.MAPWIDTH):
                tile_x = (x * self.sim.SPRITE_SIZE) - self.camera.cam_x
                tile_y = (y * self.sim.SPRITE_SIZE) - self.camera.cam_y
                if self.onscreen(tile_x, tile_y):
                    self.Tiles[y][x].rect.topleft = (tile_x, tile_y)

        self.bg_sprites.draw(self.sim.background)

    def draw_plants(self):
        for plant in self.plants:
            tile_x = (plant.x_pos * self.sim.SPRITE_SIZE) - self.camera.cam_x
            tile_y = (plant.y_pos * self.sim.SPRITE_SIZE) - self.camera.cam_y
            if self.onscreen(tile_x, tile_y):
                plant.rect.topleft = (tile_x, tile_y)

        self.plants.draw(self.sim.background)

    def draw_animals(self):
        for animal in self.animals:
            tile_x = (animal.x_pos * self.sim.SPRITE_SIZE) - self.camera.cam_x
            tile_y = (animal.y_pos * self.sim.SPRITE_SIZE) - self.camera.cam_y
            if self.onscreen(tile_x, tile_y):
                animal.rect.topleft = (tile_x, tile_y)

        self.animals.draw(self.sim.background)

    def onscreen(self, x, y):
        return not (x < self.sim.SPRITE_SIZE or x > self.sim.SCREENWIDTH) or\
                    (y < self.sim.SPRITE_SIZE or y > self.sim.SCREENHEIGHT)

# Safari Loop
#--------------------------------------------------------------------------------

    def loop(self):
        x = 0
        while True:

            print("tick: " + x.__str__())
            self.map_tick()
            self.draw_map()
            x += 1
            pygame.time.wait(500)
            if x == self.sim.NUM_ITERATIONS:
                self.sim.FLORA_COUNT = 0
                self.sim.FAUNA_COUNT = 0
                return

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.NOEVENT:
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.camera.cam_x -= 50
                    if event.key == pygame.K_RIGHT:
                        self.camera.cam_x += 50
                    if event.key == pygame.K_DOWN:
                        self.camera.cam_y += 50
                    if event.key == pygame.K_UP:
                        self.camera.cam_y -= 50



# Camera Helper Class, Determines what is "onscreen" at any given time
# --------------------------------------------------------------------------------------
class Camera():

    def __init__(self, x, y):
        self.cam_x = x
        self.cam_y = y
