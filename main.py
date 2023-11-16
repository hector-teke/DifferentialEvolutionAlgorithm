import random


# rand/1/bin        CR = 0.3; F = 0.5

class Individual:
    def __init__(self):
        self.values = []
        self.quality = None
        self.mutationCons = None
        self.crossoverProb = None

    def __str__(self):
        return f"values={self.values}, quality={self.quality}, mutationCons={self.mutationCons}, crossoverProb={self.crossoverProb})"


def create_first(bound=5.12, population=20, dimension=10):  # Returns the first population of solutions
    solutions = []

    for i in range(population):
        ind = Individual()
        for j in range(dimension):
            ind.values.append(random.uniform(- bound, bound))

        solutions.append(ind)
        print(solutions[i])

    return solutions


def select_best(function, solutions):
    best = None
    max = 0.0

    for ind in solutions:
        ind.quality = function(ind.values)

        if ind.quality > max:
            max = ind.quality
            best = ind

    return best


def mutation(x, mutationCons):
    ind = Individual()
    return ind


def crossover(x1, x2, crossoverProb):
    ind = Individual()
    return ind


def differential_evolution(function, generations=1000, bound=5.12, population=20, dimension=10, crossoverProb=0.3, mutationCons=0.5):
    # Pseudo-random generation of population
    solutions = create_first(bound, population, dimension)
    new_solutions = []
    history = []
    best = select_best(function, solutions)  # Select best solution from population
    history.append(best)

    for g in range(generations):  # For every iteration

        for i in range(population):  # For each element in population
            xi = solutions[i]
            vi = mutation(xi, mutationCons)
            ui = crossover(xi, vi, crossoverProb)

            if function(ui.values) > function(xi.values):     # Maximise the quality
                new_solutions[i] = ui
            else:                                             # Decides which one survives
                new_solutions[i] = xi

            solutions = new_solutions
            new_solutions = []
            best = select_best(function, solutions)
            history.append(best)

            if function(best) == 0:  # Stops the algorithm if the best is found
                return best

    return best, history


def suma(s):  # Funcion chorra
    return sum(s)


if __name__ == '__main__':
    # print(differential_evolution(sum))

    create_first(5, 5, 8)
