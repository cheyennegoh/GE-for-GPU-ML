# ge.py

from datasets import mkspiral

from instructions.fp32 import add, sub, mul, div, sin, cos, if_gt

import grape.grape as grape
import grape.algorithms as algorithms

from deap import creator, base, tools

# DEBUG
import sys

import os
import subprocess
from pathlib import Path
import tempfile
import struct

import numpy as np
import random

import textwrap
import csv

from sklearn.model_selection import train_test_split

import warnings
warnings.filterwarnings("ignore")


def setDataSet(RANDOM_SEED):
    data = mkspiral()
    X = data[:,:-1]
    Y = data[:,-1]

    X_train, X_test, Y_train, Y_test = train_test_split(X, 
                                                        Y, 
                                                        test_size=0.2, 
                                                        random_state=RANDOM_SEED)

    BNF_GRAMMAR = grape.Grammar("grammar.bnf")

    return X_train, Y_train, X_test, Y_test, BNF_GRAMMAR


def mae(y, yhat):
    """
    Calculate mean absolute error between inputs.

    :param y: The expected input (i.e. from dataset).
    :param yhat: The given input (i.e. from phenotype).
    :return: The mean absolute error.
    """
    
    compare = np.equal(y, yhat)

    return 1 - np.mean(compare)


def generate_c_code(x, expression):
    subarrays = []
    for row in x:
        subarrays.append(''.join(['{', ', '.join([str(val) for val in row.tolist()]), '}']))
    
    declare_input_array = ''.join([f'float x[{x.shape[0]}][{x.shape[1]}] = ', '{', ', '.join(subarrays), '}'])

    indented_expression = '\n'.join([f'\t{line}' for line in expression.splitlines()])

    include = ('#include <math.h>\n'
               '#include <stdio.h>\n'
               '#include <string.h>\n')
    
    write_data = ('void write_data(char *filename, float *data, size_t size)\n'
                  '{\n'
                  '\tFILE *file = fopen(filename, "wb");\n'
                  '\tfwrite(data, sizeof(float), size, file);\n'
                  '\tfclose(file);\n'
                  '}\n')

    evaluate = (f'float evaluate(float x[{x.shape[1]}])\n'
                '{\n'
                f'\tfloat r[6];\n'
                f'\tmemset(r, 0, sizeof(float) * 6);\n'
                f'\tmemcpy(r, x, sizeof(float) * {x.shape[1]});\n\n'
                f'{indented_expression}\n\n'
                f'\treturn r[0];\n'
                '}\n')
    
    main = (f'int main(int argc, char *argv[])\n'
            '{\n'
            f'\t{declare_input_array};\n\n'
            f'\tfloat pred[{x.shape[0]}];\n\n'
            f'\tfor (int i = 0; i < {x.shape[0]}; i++)\n'
            '\t{\n'
            f'\t\tpred[i] = evaluate(x[i]);\n'
            '\t}\n\n'
            '\tif (argc > 1)\n'
            '\t{\n'
            f'\t\twrite_data(argv[1], pred, {x.shape[0]});\n'
            '\t}\n\n'
            '\treturn 0;\n\n'
            '}\n')
    
    return '\n'.join([include, write_data, evaluate, main])


def run_c_program(x, expression):
    tmpdir = tempfile.TemporaryDirectory()

    try:
        code = generate_c_code(x, expression)
        program_path = os.path.join(tmpdir.name, 'program.c')
        with open(program_path, 'w') as f:
            f.write(code)

        executable_path = os.path.join(tmpdir.name, 'executable')
        subprocess.run(['gcc', program_path, '-o', executable_path])

        data_path = os.path.join(tmpdir.name, 'data.bin')
        subprocess.run([executable_path, data_path])
        
        with open(data_path, "rb") as file:
            file_content = file.read()
            array = struct.unpack(f'{len(file_content) // struct.calcsize('f')}f', 
                                file_content)
    
    finally:
        tmpdir.cleanup()

    return np.array(array)


def fitness_eval(individual, points):
    x = points[0]
    Y = points[1]

    if individual.invalid == True:
        return np.NaN,

    # Evaluate the expression
    expression = eval(individual.phenotype)
    assert np.isrealobj(expression)

    pred = run_c_program(x, expression)

    try:
        Y_class = [1 if pred[i] > 0 else 0 for i in range(len(Y))]
    except (IndexError, TypeError):
        return np.NaN,
    fitness = mae(Y, Y_class)
    
    return fitness,


toolbox = base.Toolbox()

# Single objective, minimising
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))

creator.create("Individual", grape.Individual, fitness=creator.FitnessMin)

toolbox.register("populationCreator", grape.sensible_initialisation, creator.Individual)

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
MIN_INIT_TREE_DEPTH = 5
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
    print(f"\n\nRun: {i}\n")

    RANDOM_SEED = i

    X_train, Y_train, X_test, Y_test, BNF_GRAMMAR = setDataSet(RANDOM_SEED)

    np.random.seed(RANDOM_SEED)
    random.seed(RANDOM_SEED)

    population = toolbox.populationCreator(pop_size=POPULATION_SIZE,
                                           bnf_grammar=BNF_GRAMMAR,
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
                                                            mutpb=P_MUTATION,
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
                                                            genome_representation=GENOME_REPRESENTATION,
                                                            stats=stats,
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

    Path(r"./results/").mkdir(parents=True, exist_ok=True)

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
