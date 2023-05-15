import operator

from Particle import Particle


class PSO:
    def __init__(self, objective_function, n_particles=100):
        self.g = None
        self.population = list()
        self.objective_function = objective_function
        for i in range(n_particles):
            particle = Particle()
            particle.evaluate(self.objective_function)
            self.population.append(particle)
        self.g = max(self.population, key=operator.attrgetter('evaluation_best'))

    def run(self, n_steps=1000):
        for t in range(n_steps):
            for particle in self.population:
                particle.update_velocity(self.g)
                particle.evaluate(self.objective_function)
                temp_g = max(self.population, key=operator.attrgetter('evaluation_best'))
                if temp_g.p_best < self.g.p_best:
                    self.g = temp_g
            print("Step {}: G={}".format(t, self.g))
