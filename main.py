import random


# rand/1/bin        CR = 0.3; F = 0.5

def create_first(length=50, population=50):  # Returns the first population of solutions
    solutions = []

    for i in range(population):
        s = ""
        for j in range(length):
            s += str(random.randint(0, 1))

        solutions.append(s)

    return solutions

def select_best(function, solutions):
    best = solutions[0]
    quality = function(best)

    for i in range(1, len(solutions)):
        aux = function(solutions[i])

        if aux > quality:
            best = solutions[i]
            quality = aux
    return best

def mutation(x, mutationCons):

    return ''

def crossover(x1, x2, crossoverProb):

    return ''

def differential_evolution(function, generations=1000, lenght=50, population=50, crossoverProb=0.3, mutationCons=0.5):

    # Pseudo-random generation of population
    p = create_first(lenght, population)
    new_p = []
    best = select_best(function, p)  # Select best solution from population

    for g in range(generations):    # At every iteration

        for i in range(population):         # For each element in population
            xi = p[i]
            vi = mutation(xi, mutationCons)
            ui = crossover(xi, vi, crossoverProb)

            if function(ui) < function(xi):
                new_p[i] = ui
            else:
                new_p[i] = xi

            p = new_p
            new_p = []
            best = select_best(function, p)

            if function(best) == 0:     # Stops the algorithm if the best is found
                return best

    return best



def funcion(s):
    num = int(s, 2)
    return num





if __name__ == '__main__':

    print(differential_evolution(funcion))





