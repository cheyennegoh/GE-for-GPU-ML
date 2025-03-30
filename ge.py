import grape.grape as grape
import grape.algorithms as algorithms

from deap import creator, base, tools

import numpy as np
import random

import textwrap
import csv

import warnings
warnings.filterwarnings("ignore")

# TODO: Write fitness function
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

REPORT_ITEMS = ['gen',
                'invalid',
                'avg',
                'std',
                'min',
                'max',
                'fitness_test',
                'best_ind_length',
                'avg_length',
                'best_ind_nodes',
                'avg_nodes',
                'best_ind_depth',
                'avg_depth',
                'avg_used_codons',
                'best_ind_used_codons',
                'structural_diversity',
                'selection_time',
                'generation_time']

N_RUNS = 1

for i in range(N_RUNS):
    print("\n\nRun: {i}\n")

    RANDOM_SEED = i
    np.random.seed(RANDOM_SEED)
    random.seed(RANDOM_SEED)

    # TODO: Set dataset and grammar
    X_train = None
    Y_train = None
    X_test = None
    Y_test = None
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

    population, logbook = algorithms.ge_eaSimpleWithElitism(population,
                                                            toolbox,
                                                            cxpb=P_CROSSOVER,
                                                            ngen=MAX_GENERATIONS,
                                                            elite_size=ELITE_SIZE,
                                                            bnf_grammar=BNF_GRAMMAR,
                                                            codon_size=CODON_SIZE,
                                                            max_tree_depth=MAX_TREE_DEPTH,
                                                            max_genome_length=MAX_GENOME_LENGTH,
                                                            points_train=[X_train, Y_train],
                                                            points_test=[X_test, Y_test],
                                                            codon_consumption=CODON_CONSUMPTION,
                                                            report_items=REPORT_ITEMS,
                                                            genome_represation=GENOME_REPRESENTATION,
                                                            stat=stats,
                                                            halloffame=hof,
                                                            verbose=False)
    
    best = hof.items[0].phenotype

    print("Best individual: \n", "\n".join(textwrap.wrap(best, 80)))
    print("\nTraining Fitness: ", hof.items[0].fitness.values[0])
    print("Test Fitness: ", fitness_eval(hof.items[0], [X_test, Y_test])[0])
    print("Depth: ", hof.items[0].depth)
    print("Length of the genome: ", len(hof.items[0].genome))
    print(f"Used portion of the genome: {hof.items[0].used_codons/len(hof.items[0].genome):.2f}")

    max_fitness_values, mean_fitness_values = logbook.select("max", "avg")
    min_fitness_values, std_fitness_values = logbook.select("min", "std")
    best_ind_length = logbook.select("best_ind_length")
    avg_length = logbook.select("avg_length")
    selection_time = logbook.select("selection_time")
    generation_time = logbook.select("generation_time")
    gen, invalid = logbook.select("gen", "invalid")
    avg_used_codons = logbook.select("avg_used_codons")
    best_ind_used_codons = logbook.select("best_ind_used_codons")
    fitness_test = logbook.select("fitness_test")
    best_ind_nodes = logbook.select("best_ind_nodes")
    avg_nodes = logbook.select("avg_nodes")
    best_ind_depth = logbook.select("best_ind_depth")
    avg_depth = logbook.select("avg_depth")
    structural_diversity = logbook.select("structural_diversity")

    r = RANDOM_SEED
    header = REPORT_ITEMS

    with open(r"./results/" + str(r) + ".csv", "w", encoding='UTF8', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter='\t')
        writer.writerow(header)

        for value in range(len(max_fitness_values)):
            writer.writerow([gen[value],
                             invalid[value],
                             mean_fitness_values[value],
                             std_fitness_values[value],
                             min_fitness_values[value],
                             max_fitness_values[value],
                             fitness_test[value],
                             best_ind_length[value],
                             avg_length[value],
                             best_ind_nodes[value],
                             avg_nodes[value],
                             best_ind_depth[value],
                             avg_depth[value],
                             avg_used_codons[value],
                             structural_diversity[value],
                             selection_time[value],
                             generation_time[value]])
