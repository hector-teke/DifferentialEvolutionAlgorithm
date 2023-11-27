import random
from functions import ObjFunction

# rand/1/bin        CR = 0.3; F = 0.5

class Individual:
    def __init__(self):
        self.values = []
        self.quality = None
        self.mutationCons = None
        self.crossoverProb = None

    def __str__(self):
        return f"values={self.values}, quality={self.quality}, mutationCons={self.mutationCons}, crossoverProb={self.crossoverProb})"


def create_first(bound=5.12, population=20, dimension=10, mutationCons=0.5, crossoverProb=0.3):  # Returns the first population of solutions
    solutions = []

    for i in range(population):
        ind = Individual()
        for j in range(dimension):
            ind.values.append(round(random.uniform(- bound, bound), 4))
            ind.crossoverProb = crossoverProb
            ind.mutationCons = mutationCons

        solutions.append(ind)

    return solutions


def select_best(function, solutions):
    best = None
    max = 0.0

    for ind in solutions:

        if ind.quality is None:  # Avoid repeating the evaluation
            ind.quality = function(ind.values)

        if ind.quality > max:
            max = ind.quality
            best = ind

    return best


def mutation(x, solutions):   #It returns a vector (not an individual)
    # Select 3 mutually different individuals randomly (different from the parent x)
    r1, r2, r3 = select_3(x, solutions)
    mutationCons = x.mutationCons   # Takes the value from the individual

    # Mutation vector calculation
    vector = []
    for i in range(len(x.values)):
        vector.append(round(r1.values[i] + mutationCons * (r2.values[i] - r3.values[i]), 4))

    return vector


def select_3(x, solutions):
    aux = solutions.copy()

    aux.remove(x)  # Drops x from the copy

    selection = random.sample(aux, 3)  # Choose 3 different individuals

    return selection


def crossover(xi, vi):   #xi is an individual but vi is a vector
    ui = Individual()
    crossoverProb = xi.crossoverProb

    ui.mutationCons = xi.mutationCons
    ui.crossoverProb = crossoverProb

    if crossoverProb == 0:
        ui.values = xi.values.copy()
        pos = random.randint(0, len(vi) - 1)
        ui.values[pos] = vi[pos]
    else:
        for i in range(0, len(vi)):
            ran = random.uniform(0, 1)
            if ran <= crossoverProb:
                ui.values.append(vi[i])
            else:
                ui.values.append(xi.values[i])

    return ui


def differential_evolution(function, generations=1000, bound=5.12, population=20, dimension=10, crossoverProb=0.3, mutationCons=0.5, jDE=False):
    # Pseudo-random generation of population
    solutions = create_first(bound, population, dimension, mutationCons, crossoverProb)
    new_solutions = []
    history = []
    best = select_best(function, solutions)  # Select best solution from population
    history.append(best)

    for g in range(generations):  # For every iteration

        for i in range(population):  # For each element in population
            xi = solutions[i]

            # Adaptative variant: changes on F and CR may occur here with prob=0.1


            vi = mutation(xi, solutions)
            ui = crossover(xi, vi)

            # Make sure that values are in the bounds
            for j in range(len(ui.values) - 0):
                val = ui.values[j]
                if val < -bound or val > bound:
                    ui.values[j] = round(random.uniform(- bound, bound), 4)

            if function(ui.values) > function(xi.values):  # Maximise the quality

                # Adaptative variant: If the new individual is better, we keep the new F and CR as well

                new_solutions.append(ui)
            else:  # Decides which one survives

                # Adaptative variant: If the new individual is worst, we keep the old F and CR

                new_solutions.append(xi)

        solutions = new_solutions
        new_solutions = []
        best = select_best(function, solutions)
        history.append(best)

        if function(best.values) == 1:  # Stops the algorithm if the best is found (or it is really close)
            print("Stopped at generation ", g)
            return best, history

    return best, history


if __name__ == '__main__':

    f = ObjFunction()
    best, history = differential_evolution(f.schwefel, bound=500, jDE=False)
    print(best)





"""    s = create_first(5, 20, 10)
    best = select_best(sum, s)

    print(best)

    mut = mutation(best, s)
    print(mut)

    cross = crossover(best, mut, 0.3)
    print(cross)"""












