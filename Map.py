__author__ = 'lkavanagh010'
import pygame, random
from Tiles import Grass, Water



class Map():

    HEIGHTS = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def chance_of_grass(self, height):
        if   height == 0: return  30
        elif height <= 3: return 50
        elif height <= 4: return 80
        elif height <= 7: return 95

        return 100

    def __init__(self, width, height):
        self.MAPWIDTH = width
        self.MAPHEIGHT = height
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

class Camera():

    def __init__(self, x, y):
        self.cam_x = x
        self.cam_y = y
        self.moveleft = False
        self.moveright = False
        self.moveup = False
        self.movedown = False

    def pan_camera(self):
        if self.movedown:
            self.cam_y += 5
        if self.moveup:
            self.cam_y -= 5
        if self.moveleft:
            self.cam_x -= 5
        if self.moveright:
            self.cam_x += 5
