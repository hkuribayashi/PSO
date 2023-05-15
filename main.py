from PSO import PSO


def function_1(x):
    x = round(x, 2)
    y = -2.0 * (x ** 2.0) + 10.0
    return y


def function_2(x):
    x = round(x, 2)
    y = -1.0 * (x ** 2.0) + 2.0 * x + 3.0
    return y


pso = PSO(function_1, 200)
pso.run(n_steps=100)

print("Result (G particle): {}".format(pso.g))
