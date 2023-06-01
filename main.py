from PSO import PSO


def function_1(vetor):
    y = 0
    for xi in vetor:
        y += xi ** 2
    return y


pso = PSO(function_1, 200)
pso.run(n_steps=100)

print("Result (G particle): {}".format(pso.g))
