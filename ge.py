# ge.py

import datasets
import codegen

from instructions.fp32 import add, sub, mul, pdiv, sin, cos, if_gt

import grape.grape as grape
import grape.algorithms as algorithms

from deap import creator, base, tools

# DEBUG
import sys

from pathlib import Path

import numpy as np
import random

import csv
import json

from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle

import warnings
warnings.filterwarnings("ignore")


def set_dataset(problem, random_seed=None, test_size=0):
    if problem == 'spiral':
        data = datasets.mkspiral()

    X = data[:,:-1]
    Y = data[:,-1]

    if test_size == 0:
        X, Y = shuffle(X, Y, random_state=random_seed)
        
        return X, Y
    
    else:
        X_train, X_test, Y_train, Y_test = train_test_split(X, 
                                                            Y, 
                                                            test_size=test_size, 
                                                            random_state=random_seed)

        return X_train, Y_train, X_test, Y_test


def set_grammar(problem, compiler, n_registers):
    basename = '_'.join((problem, compiler, str(n_registers))) + '.bnf'
    return grape.Grammar('./grammars/' + basename)


def mae(y, yhat):
    """
    Calculate mean absolute error between inputs.

    :param y: The expected input (i.e. from dataset).
    :param yhat: The given input (i.e. from phenotype).
    :return: The mean absolute error.
    """
    
    compare = np.equal(y, yhat)

    return 1 - np.mean(compare)


def evaluate_expression(phenotype):
    expression = eval(phenotype)

    assert np.isrealobj(expression)

    return expression


def fitness_eval(population, points, train=True):
    (x, Y), compiler, n_registers = points

    expressions = []
    for individual in population:
        if (train and individual.fitness.valid) or individual.invalid:
            continue
        
        expressions.append(evaluate_expression(individual.phenotype))

    pred = codegen.run_program(x, expressions, compiler, n_registers)

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


def run_algorithm(X_train, Y_train, problem, compiler, n_registers, pop_size, 
                  ngen, cxpb, mutpb, elite_size, hof_size, tournsize, 
                  max_init_depth, min_init_depth, max_tree_depth, run=0, 
                  export_results=False):
    
    bnf_grammar = set_grammar(problem, compiler, n_registers)

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
                                                            points_train=([X_train, Y_train], 
                                                                          compiler, 
                                                                          n_registers),
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


def multiple_runs(X_train, Y_train, problem, compiler, n_registers, pop_size, 
                  ngen, cxpb, mutpb, elite_size, hof_size, tournsize, 
                  max_init_depth, min_init_depth, max_tree_depth, n_runs=30, 
                  export_results=True):
    
    for run in range(n_runs):
        print(f"\nRun: {run}\n")

        np.random.seed(run)
        random.seed(run)

        run_algorithm(X_train, Y_train, problem, compiler, n_registers, 
                      pop_size, ngen, cxpb, mutpb, elite_size, hof_size, 
                      tournsize, max_init_depth, min_init_depth, 
                      max_tree_depth, run, export_results)


def main():

    path = None
    
    with open(path) as jsonfile:
        json_data = json.load(jsonfile)
    
    params = json_data['params']
    
    X, y = set_dataset(params['problem'])

    multiple_runs(X, y, **params)

    with open(r"./results/" + "params.json", "w") as jsonfile:
        json.dump({'params': params}, jsonfile, indent=4)


if __name__ == "__main__":
    main()