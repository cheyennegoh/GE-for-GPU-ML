import grape.grape as grape
import grape.algorithms as algorithms

from deap import creator, base, tools

import numpy as np
import random

import warnings
warnings.filterwarnings("ignore")

def fitness_eval(individual, points):
    return

toolbox = base.Toolbox()

# Single objective, minimising
creator.create("FitnessMin", base.Fitness, weights=(-1.0))

creator.create("Individual", grape.Individual, fitness=creator.FitnessMin)

toolbox.register("populationCreator", grape.sensible_initialisation, creator.Indivdual)

toolbox.register("evaluate", fitness_eval)

# Tournament selection
toolbox.register("select", tools.selTournament, tournsize=7)

# One-point crossover
toolbox.register("mate", grape.crossover_onepoint)

# Flip-int mutation
toolbox.register("mutate", grape.mutation_int_flip_per_codon)

POPULATION_SIZE = 200
MAX_GENERATIONS = 200
P_CROSSOVER = 0.8
P_MUTATION = 0.01
ELITE_SIZE = 0
HALLOFFAME_SIZE = 1

MAX_INIT_TREE_DEPTH = 13
MIN_INIT_TREE_DEPTH = 3
MAX_TREE_DEPTH = 35
MAX_WRAPS = 0
CODON_SIZE = 255

CODON_CONSUMPTION = 'lazy'
GENOME_REPRESENTATION = 'list'
MAX_GENOME_LENGTH = None

N_RUNS = 1

for i in range(N_RUNS):
    print("\n\nRun: {i}\n")

    RANDOM_SEED = i
    np.random.seed(RANDOM_SEED)
    random.seed(RANDOM_SEED)

    # TODO: Set dataset and grammar
    BNF_GRAMMAR = None

    population = toolbox.populationCreator(pop_size=POPULATION_SIZE,
                                           min_init_depth=MIN_INIT_TREE_DEPTH,
                                           max_init_depth=MAX_INIT_TREE_DEPTH,
                                           codon_size=CODON_SIZE,
                                           codon_consumption=CODON_CONSUMPTION,
                                           genome_representation=GENOME_REPRESENTATION)

    hof = tools.HallOfFame(HALLOFFAME_SIZE)

    stats = tools.Statistics(key=lambda ind: ind.fitness.values)
    stats.register("avg", np.nanmean)
    stats.register("std", np.nanstd)
    stats.register("min", np.nanmin)
    stats.register("max", np.nanmax)