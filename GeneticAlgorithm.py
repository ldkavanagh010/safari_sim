import numpy as np
import pygame
from Fauna import Gazelle

__author__ = 'lkavanagh010'

class Algorithm():

    def __init__(self, sim):
        self.sim = sim
        self.animals = self.sim.map.animals
        self.alg = "darwin"

        self.propagate()



    def propagate(self):
        if self.alg == "darwin":
            self.animals = self.darwin_helper()

    def darwin_helper(self):
        #setup, temporary variables for computation
        temp = pygame.sprite.Group()
        fitness = 0
        fit = None
        second = None
        # find the two fittest individuals in the pack
        for sprite in self.animals:
            if sprite.fitness > fitness:
                fitness = sprite.fitness
                if fit is not None:
                    second = fit
                    fit = sprite
                else:
                    fit = sprite
        # remove the specimens from the herd and lop out their brains
        fit.kill()
        second.kill()
        brain1 = fit.brain
        brain2 = second.brain
        # create two children based on their theta values
        temp.add(self.breed(brain1, brain2))
        temp.add(self.breed(brain2, brain1))

        # continue until old generation is unpopulated and new generated is populated
        if self.animals.has():
            return self.darwin_helper()
        else:
            return temp


    def breed(self, br1, br2):
        # theta values of brain 1
        theta_in_1 = br1.theta_in
        theta_out_1 = br1.theta_out

        # theta values for brain 2
        theta_in_2 = br2.theta_in
        theta_out_2 = br2.theta_out

        # the child in need of a transplant from his parents
        child = Gazelle(self.sim.map)

        # the transplant
        child.brain.theta_in = np.add(theta_in_1, theta_in_2)
        child.brain.theta_in = child.brain.theta_in/2
        print(child.brain.theta_in)

        child.brain.theta_out = np.add(theta_out_1, theta_out_2)
        child.brain.theta_out = child.brain.theta_out/2
        print(child.brain.theta_out)



        return child


