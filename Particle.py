import math
import random
import numpy as np


class Particle:
    def __init__(self, n_dimensoes=10, inf_limit=-10, upper_limit=10):
        self.v = 0
        self.p = np.zeros(n_dimensoes)
        self.p_best = 0
        self.evaluation = 0

        # iniciar a posicao e a velocidade:
        for x in self.p:
            x = random.uniform(inf_limit, upper_limit)
        self.v = 0
        self.evaluation_best = self.p

    def evaluate(self, objective_function):
        self.evaluation = objective_function(self.p)
        if self.evaluation < self.evaluation_best:
            self.evaluation_best = self.evaluation
            self.p_best = self.p

    def update_velocity(self, g):
        c1 = 2.05
        c2 = 2.05
        c = c1 + c2
        x = 2/(2-c-math.sqrt(c**2 + 4*c))
        r1 = random.uniform(0, 1)
        r2 = random.uniform(0, 1)
        self.v += + c1 * r1 * (self.p_best - self.p)
        self.v += c2 * r2 * (g.p_best - self.p)
        new_v = round(x * self.v, 2)
        self.p += new_v

    def __str__(self):
        return "Particle [p={}]".format(self.p)
