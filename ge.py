# ge.py

from datasets import mkspiral

from instructions.fp32 import add, sub, mul, pdiv, sin, cos, if_gt

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

import csv

from sklearn.model_selection import train_test_split

import warnings
warnings.filterwarnings("ignore")


def setDataSet(random_seed=None, test_size=0.2):
    data = mkspiral()
    X = data[:,:-1]
    Y = data[:,-1]

    bnf_grammar = grape.Grammar("grammar.bnf")

    if test_size == 0:
        return X, Y, bnf_grammar
    
    else:
        X_train, X_test, Y_train, Y_test = train_test_split(X, 
                                                            Y, 
                                                            test_size=0.2, 
                                                            random_state=random_seed)

        return X_train, Y_train, X_test, Y_test, bnf_grammar


def mae(y, yhat):
    """
    Calculate mean absolute error between inputs.

    :param y: The expected input (i.e. from dataset).
    :param yhat: The given input (i.e. from phenotype).
    :return: The mean absolute error.
    """
    
    compare = np.equal(y, yhat)

    return 1 - np.mean(compare)


def generate_c_code(x, expressions):
    include = ('#include <math.h>\n'
               '#include <stdio.h>\n'
               '#include <string.h>\n')
    
    write_data = ('void write_data(char *filename, float *data, size_t size)\n'
                  '{\n'
                  '\tFILE *file = fopen(filename, "wb");\n'
                  '\tfwrite(data, sizeof(float), size, file);\n'
                  '\tfclose(file);\n'
                  '}\n')

    evaluate = ''
    for i, expression in enumerate(expressions):
        indented_expression = '\n'.join([f'\t{line}' for line in expression.splitlines()])

        evaluate += (f'float evaluate{i}(float x[{x.shape[1]}])\n'
                     '{\n'
                     f'\tfloat r[6];\n'
                     f'\tmemset(r, 0, sizeof(float) * 6);\n'
                     f'\tmemcpy(r, x, sizeof(float) * {x.shape[1]});\n\n'
                     f'{indented_expression}\n\n'
                     f'\treturn r[0];\n'
                     '}\n')

    subarrays = []
    for row in x:
        subarrays.append(''.join(['{', ', '.join([str(val) for val in row.tolist()]), '}']))
    
    declare_input_array = ''.join([f'float x[{x.shape[0]}][{x.shape[1]}] = ', '{', ', '.join(subarrays), '}'])

    pred = ''
    for i in range(len(expressions)):
        pred += f'\t\tpred[{i}][i] = evaluate{i}(x[i]);\n'

    main = (f'int main(int argc, char *argv[])\n'
            '{\n'
            f'\t{declare_input_array};\n\n'
            f'\tfloat pred[{len(expressions)}][{x.shape[0]}];\n\n'
            f'\tfor (int i = 0; i < {x.shape[0]}; i++)\n'
            '\t{\n'
            f'{pred}'
            '\t}\n\n'
            '\tif (argc > 1)\n'
            '\t{\n'
            f'\t\twrite_data(argv[1], (float *)pred, {len(expressions)} * {x.shape[0]});\n'
            '\t}\n\n'
            '\treturn 0;\n\n'
            '}\n')
    
    return '\n'.join([include, write_data, evaluate, main])


def run_c_program(x, expressions):
    tmpdir = tempfile.TemporaryDirectory()

    try:
        code = generate_c_code(x, expressions)
        program_path = os.path.join(tmpdir.name, 'program.c')
        with open(program_path, 'w') as f:
            f.write(code)

        executable_path = os.path.join(tmpdir.name, 'executable')
        subprocess.run(['gcc', program_path, '-lm', '-o', executable_path])

        data_path = os.path.join(tmpdir.name, 'data.bin')
        subprocess.run([executable_path, data_path])
        
        with open(data_path, "rb") as file:
            file_content = file.read()
            array = struct.unpack(f'{len(file_content) // struct.calcsize("f")}f', 
                                  file_content)
    
    finally:
        tmpdir.cleanup()

    return np.array(array).reshape((len(expressions), x.shape[0]))


def evaluate_expression(phenotype):
    expression = eval(phenotype)

    assert np.isrealobj(expression)

    return expression


def fitness_eval(population, points, train=True):
    x = points[0]
    Y = points[1]

    expressions = []
    for individual in population:
        if (train and individual.fitness.valid) or individual.invalid:
            continue
        
        expressions.append(evaluate_expression(individual.phenotype))

    pred = run_c_program(x, expressions)

    fitnesses = []
    i = 0
    for individual in population:
        if train and individual.fitness.valid:
            continue

        if individual.invalid:
            fitness = np.NaN
        else:
            try:
                Y_class = [1 if pred[i][j] > 0 else 0 for j in range(len(Y))]
            except (IndexError, TypeError):
                fitness = np.NaN
            
            fitness = mae(Y, Y_class)
            i += 1
    
        if train:
            individual.fitness.values = fitness,
        else:
            fitnesses.append(fitness)

    if not train:
        return fitnesses


def create_toolbox(tournsize):
    toolbox = base.Toolbox()

    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", grape.Individual, fitness=creator.FitnessMin)
    toolbox.register("populationCreator", grape.sensible_initialisation, creator.Individual)
    toolbox.register("evaluate", fitness_eval)
    toolbox.register("select", tools.selTournament, tournsize=tournsize)
    toolbox.register("mate", grape.crossover_onepoint)
    toolbox.register("mutate", grape.mutation_int_flip_per_codon)

    return toolbox


def create_stats():
    stats = tools.Statistics(key=lambda ind: ind.fitness.values)

    stats.register("avg", np.nanmean)
    stats.register("std", np.nanstd)
    stats.register("min", np.nanmin)
    stats.register("max", np.nanmax)

    return stats


def display_best(hof):
    print("\nBest individual:\n" + eval(hof.items[0].phenotype))
    print("\nTraining Fitness: ", hof.items[0].fitness.values[0])
    print("Depth: ", hof.items[0].depth)
    print("Length of the genome: ", len(hof.items[0].genome))
    print(f"Used portion of the genome: {hof.items[0].used_codons/len(hof.items[0].genome):.2f}\n")


def record_results(run, report_items, ngen, logbook):
    Path(r"./results/").mkdir(parents=True, exist_ok=True)

    with open(r"./results/" + str(run) + ".csv", "w", encoding='UTF8', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter='\t')
        writer.writerow(report_items)
        
        for value in range(ngen + 1):
            writer.writerow([logbook.select(item)[value] for item in report_items])


def run_algorithm(X_train, Y_train, bnf_grammar, pop_size, ngen, cxpb, 
                  mutpb, elite_size, hof_size, tournsize, max_init_depth, 
                  min_init_depth, max_tree_depth, run=0, export_results=False):

    codon_size = 255
    codon_consumption = 'lazy'
    genome_representation = 'list'

    report_items = ['gen', 'invalid', 'avg', 'std', 'min', 'max',
                    'best_ind_length', 'avg_length','best_ind_nodes', 'avg_nodes',
                    'best_ind_depth', 'avg_depth', 'avg_used_codons',
                    'best_ind_used_codons', 'structural_diversity',
                    'selection_time', 'generation_time']

    toolbox = create_toolbox(tournsize=tournsize)

    population = toolbox.populationCreator(pop_size=pop_size,
                                           bnf_grammar=bnf_grammar,
                                           min_init_depth=min_init_depth,
                                           max_init_depth=max_init_depth,
                                           codon_size=codon_size,
                                           codon_consumption=codon_consumption,
                                           genome_representation=genome_representation)

    hof = tools.HallOfFame(hof_size)

    stats = create_stats()

    population, logbook = algorithms.ge_eaSimpleWithElitism(population,
                                                            toolbox,
                                                            cxpb=cxpb,
                                                            mutpb=mutpb,
                                                            ngen=ngen,
                                                            elite_size=elite_size,
                                                            bnf_grammar=bnf_grammar,
                                                            codon_size=codon_size,
                                                            max_tree_depth=max_tree_depth,
                                                            max_genome_length=None,
                                                            points_train=[X_train, Y_train],
                                                            codon_consumption=codon_consumption,
                                                            report_items=report_items,
                                                            genome_representation=genome_representation,
                                                            stats=stats,
                                                            halloffame=hof,
                                                            verbose=False)
    
    display_best(hof)

    if export_results:
        record_results(run, report_items, ngen, logbook)

    return hof.items[0]


def multiple_runs(X_train, Y_train, bnf_grammar, pop_size, ngen, cxpb, 
                  mutpb, elite_size, hof_size, tournsize, max_init_depth, 
                  min_init_depth, max_tree_depth, n_runs=30, 
                  export_results=True):
    
    for run in range(n_runs):
        print(f"\nRun: {run}\n")

        np.random.seed(run)
        random.seed(run)

        run_algorithm(X_train, Y_train, bnf_grammar, pop_size, ngen, 
                      cxpb, mutpb, elite_size, hof_size, tournsize, 
                      max_init_depth, min_init_depth, max_tree_depth, run, 
                      export_results)


# DEBUG
# X_train, Y_train, X_test, y_test, bnf_grammar = setDataSet()
# params = {'pop_size': 100, 'ngen': 100, 'cxpb': 0.5517681977158512, 'mutpb': 0.1501536174442644, 'elite_size': 1, 'hof_size': 8, 'tournsize': 3, 'max_init_depth': 7, 'min_init_depth': 5, 'max_tree_depth': 24}
# run_algorithm(X_train, Y_train, bnf_grammar, **params)