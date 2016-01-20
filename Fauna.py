__author__ = 'lkavanagh010'
import random
import math
from Sprite import Sprite
from Network import NeuralNetwork


class Animal(Sprite):



    def __init__(self, name, map):
        super(Animal, self).__init__(name)
        self.map = map
        self.brain = NeuralNetwork(9, 9, 5)
        self.x_pos = random.randint(0, self.map.MAPWIDTH - 1)
        self.y_pos = random.randint(0, self.map.MAPHEIGHT - 1)
        self.hunger = 0
        self.tiredness = 0
        self.distance_to_food = 0
        self.fitness = 0
        self.rect = self.image.get_rect()


# Think Outputs
#--------------------------------------------------------
    def move_up(self):
        if self.valid_move("up"):
            self.y_pos -= 1
        self.eat()

    def move_down(self):
        if self.valid_move("down"):
            self.y_pos += 1
        self.eat()

    def move_right(self):
        if self.valid_move("right"):
            self.x_pos += 1
        self.eat()

    def move_left(self):
        if self.valid_move("left"):
            self.x_pos -= 1
        self.eat()

    def sleep(self):
        self.tiredness -= 10
        self.hunger += 5

    def valid_move(self, dir):
        if self.y_pos >= 0 and self.y_pos < (self.map.MAPHEIGHT - 1) \
            and self.x_pos >= 0 and self.x_pos < (self.map.MAPWIDTH - 1):
            if (dir == "left" and self.map.Tiles[self.y_pos][self.x_pos - 1].__str__() == 'GRASS')\
                or (dir == "right" and self.map.Tiles[self.y_pos][self.x_pos + 1].__str__() == 'GRASS')\
                or (dir == "down" and self.map.Tiles[self.y_pos + 1][self.x_pos].__str__() == 'GRASS')\
                or (dir == "up" and self.map.Tiles[self.y_pos - 1][self.x_pos].__str__() == 'GRASS'):
                return True

        return False

    def eat(self):
        if self.map.Tiles[self.y_pos][self.x_pos].is_occupied:
            self.hunger -= 20
            self.fitness += 25
            p = self.map.plants.sprites()
            for eaten in p:
                if eaten.x_pos == self.x_pos and eaten.y_pos == self.y_pos:
                    self.map.plants.remove(eaten)

# Think & Helper Functions
# --------------------------------------------------------------------
    def think(self):
        self.tiredness += 5
        self.hunger += 5

        self.update_fitness()
        self.find_food()

        inputs = self.make_inputs()
        output = self.brain.feedForward(inputs)
        decision = output.index(max(output))
        if decision == 0:
            self.move_up()
        elif decision == 1:
            self.move_down()
        elif decision == 2:
            self.move_right()
        elif decision == 3:
            self.move_left()
        elif decision == 4:
            self.sleep()


    def make_inputs(self):

        inputs = [self.x_pos, self.y_pos, self.hunger, self.tiredness, self.distance_to_food]

        if self.y_pos >= 0 and self.y_pos < (self.map.MAPHEIGHT - 1) \
            and self.x_pos >= 0 and self.x_pos < (self.map.MAPWIDTH - 1):
            obstruction_left = (0 if self.map.Tiles[self.y_pos][self.x_pos - 1].__str__() == 'GRASS' else 1)
            obstruction_right = (0 if self.map.Tiles[self.y_pos][self.x_pos + 1].__str__() == 'GRASS' else 1)
            obstruction_up = (0 if self.map.Tiles[self.y_pos + 1][self.x_pos].__str__() == 'GRASS' else 1)
            obstruction_down = (0 if self.map.Tiles[self.y_pos - 1][self.x_pos].__str__() == 'GRASS' else 1)



        else:
            obstruction_left = (1 if self.x_pos == 0 else 0)
            obstruction_right = (1 if self.x_pos == self.map.MAPWIDTH else 0)
            obstruction_up = (1 if self.y_pos == 0 else 0)
            obstruction_down = (1 if self.x_pos == self.map.MAPHEIGHT else 0)

        inputs.append(obstruction_left)
        inputs.append(obstruction_right)
        inputs.append(obstruction_up)
        inputs.append(obstruction_down)
        return inputs

    def update_fitness(self):
        if self.hunger < 25:
            self.fitness += 2
        elif self.hunger < 50:
            self.fitness += 1
        if self.tiredness < 25:
            self.fitness += 2
        elif self.tiredness < 50:
            self.fitness += 1
        if self.hunger & self.tiredness < 25:
            self.fitness += 4
        elif self.hunger & self.tiredness < 50:
            self.fitness += 2

        print("fitness:" + self.fitness.__str__())

    def find_food(self):
        closest = -1
        for plant in self.map.plants:
            plant_x = plant.x_pos
            plant_y = plant.y_pos

            x_dist = plant_x - self.x_pos
            y_dist = plant_y - self.y_pos

            distance = math.sqrt((x_dist * x_dist) + (y_dist * y_dist))

            if distance < closest or distance == -1:
                closest = distance

        self.distance_to_food = closest


    def valid_fauna(self):
        if self.map.Tiles[self.y_pos][self.x_pos].__str__() == 'GRASS'\
        and self.map.Tiles[self.y_pos][self.x_pos].is_occupied == False:
            return True
        else:
            return False


class Gazelle(Animal):
    def __init__(self, map):
        super(Gazelle, self).__init__('gazelle.png', map)

class Lion(Animal):
    def __init__(self):
        super(Lion, self).__init__('lion.png')
