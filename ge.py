# ge.py

import datasets
import codegen

from instructions import add, sub, mul, pdiv, aq, swap, sin, cos, tanh, if_gt

import grape.grape as grape
import grape.algorithms as algorithms

from deap import creator, base, tools

import os
import argparse
import time
from datetime import datetime

import numpy as np
import random

import csv
import json

import warnings
warnings.filterwarnings("ignore")

# Uncomment for timing measurements
# import sys

def set_dataset(problem, n_samples=None):
    """Sets dataset for the problem.

    # Arguments
        problem: A string indicating the problem.
        n_samples: Number of samples as an integer or None.
    
    # Returns
        A tuple of NumPy arrays with train and test data.
    """
    if problem == 'spiral':
        X_train, X_test, y_train, y_test = datasets.spiral(n_samples=n_samples)
        
    elif problem == 'drive':
        X_train, X_test, y_train, y_test = datasets.drive(n_samples=n_samples)

    return X_train, y_train, X_test, y_test


def set_grammar(problem, n_registers):
    """Sets the BNF grammar file path for the problem.

    # Arguments
        problem: A string indicating the problem.
        n_registers: Number of registers as an integer.
    
    # Returns
        A grape.Grammar object.
    """
    stem = '_'.join((problem, str(n_registers)))
    return grape.Grammar(os.path.join('grammars', f'{stem}.bnf'))


def mae(y, yhat):
    """Calculates the mean absolute error between inputs.

    # Arguments
        y: The expected input from the dataset as a NumPy array.
        yhat: The given input from the phenotype as a NumPy array.
    
    # Returns
        The mean absolute error as a float.
    """
    compare = np.equal(y, yhat)

    return 1 - np.mean(compare)


def evaluate_expression(phenotype):
    """Evaluates the code expression for an individual.

    # Arguments
        phenotype: The phenotype of an individual as a string.
    
    # Returns
        The code expression as a string.
    """
    expression = eval(phenotype)

    assert np.isrealobj(expression)

    return expression


def fitness_eval(population, points, train=True):
    """Evaluates and assigns the individual fitnesses for a population.

    # Arguments
        population: A list of grape.Individual objects.
        points: A tuple containing data points, compiler, and number of 
            registers.
        train: A boolean indicating whether to train in this fitness 
            evaluation.
    
    # Returns
        Fitnesses of the population if training and otherwise None.
    """
    (x, y), compiler, n_registers = points

    expressions = []
    for individual in population:
        if (train and individual.fitness.valid) or individual.invalid:
            continue
        
        expressions.append(evaluate_expression(individual.phenotype))

    pred = codegen.run_program(x, expressions, compiler, n_registers)

    # Uncomment for timing measurements
    # print("gcc")
    # codegen.run_program(x, expressions, "gcc", n_registers)
    # print("nvcc")
    # codegen.run_program(x, expressions, "nvcc", n_registers)
    # sys.exit(0)

    fitnesses = []
    i = 0
    for individual in population:
        if train and individual.fitness.valid:
            continue

        if individual.invalid:
            fitness = np.NaN
        else:
            try:
                y_class = [0 if pred[i][j] < 0.5 else 1 for j in range(len(y))]
            except (IndexError, TypeError):
                fitness = np.NaN
            
            fitness = mae(y, y_class)
            i += 1
    
        if train:
            individual.fitness.values = fitness,
        else:
            fitnesses.append(fitness)

    if not train:
        return fitnesses


def create_toolbox(tournsize):
    """Creates a toolbox using primitive set and declared parameters.

    # Arguments
        primitiveSet: A deap.gp.PrimitiveSet object.

    # Returns
        A deap.base.Toolbox object
    """
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
    """Creates the statistics object.

    # Returns
        A deap.tools.Statistics object.
    """

    stats = tools.Statistics(key=lambda ind: ind.fitness.values)

    stats.register("avg", np.nanmean)
    stats.register("std", np.nanstd)
    stats.register("min", np.nanmin)
    stats.register("max", np.nanmax)

    return stats


def display_best(hof):
    """Prints details on the best individual.

    # Arguments
        hof: A deap.tools.HallOfFame object.

    # Returns
        None.
    """
    print("\nBest individual:\n" + eval(hof.items[0].phenotype) + "\n")
    print("Training fitness:", hof.items[0].fitness.values[0])
    print("Depth:", hof.items[0].depth)
    print("Length of the genome:", len(hof.items[0].genome))
    print(f"Used portion of the genome: {hof.items[0].used_codons / len(hof.items[0].genome):.2f}\n")


def record_results(output_path, run, report_items, ngen, logbook):
    """Writes results for the run to a CSV file.

    # Arguments
        output_path: A string containing the path for the output directory.
        run: An integer indicating the run number.
        report_items: A list of items to report.
        ngen: Total number of generations as an integer.
        logbook: A deap.tools.support.Logbook object.

    # Returns
        None.
    """
    with open(os.path.join(output_path, f'{run}.csv'), "w", encoding='UTF8', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter='\t')
        writer.writerow(report_items)
        
        for value in range(ngen + 1):
            writer.writerow([logbook.select(item)[value] for item in report_items])


def save_run_info(output_path, run, hof, duration):
    """Writes information on the run to a JSON file.

    # Arguments
        output_path: A string containing the path for the output directory.
        run: An integer indicating the run number.
        hof: A deap.tools.HallOfFame object.
        duration: The exeuction time in seconds as a float.

    # Returns
        None.
    """
    best_ind = vars(hof.items[0])
    best_ind['fitness'] = best_ind['fitness'].values[0]

    with open(os.path.join(output_path, f'{run}.json'), "w") as jsonfile:
        json.dump({'best_ind': best_ind,
                   'execution_time': duration}, jsonfile, indent=4)


def run_algorithm(X_train, y_train, problem, compiler, n_registers, pop_size, 
                  ngen, cxpb, mutpb, elite_size, hof_size, tournsize, 
                  max_init_depth, min_init_depth, max_tree_depth, run=0, 
                  output_path=None):
    """Runs the main flow of the GE algorithm.

    # Arguments
        X_train: A NumPy array containing training features.
        y_train: A NumPy array containing expected training classes.
        problem: A string indicating the problem.
        compiler: A string indicating the compiler to use.
        n_registers: Number of registers as an integer.
        pop_size: Population size as an integer.
        ngen: Number of generations as an integer.
        cxpb: Probability of crossover as a float.
        mutpb: Probability of mutation as a float.
        elite_size: Elite size as an integer.
        hof_size: Hall-of-fame size as an integer.
        tournsize: Tournament size as an integer.
        max_init_depth: Maximum initial depth as an integer.
        min_init_depth: Minimum initial depth as an integer.
        max_tree_depth: Maximum tree depth as an integer.
        run: Current run number.
        output_path: A string containing the path for the output directory or 
            None.

    # Returns
        Best individual as a grape.Individual object.
    """
    bnf_grammar = set_grammar(problem, n_registers)
    if problem == 'drive':
        n_registers += 1
    
    codon_size = 255
    codon_consumption = 'lazy'
    genome_representation = 'list'

    report_items = ['gen', 'invalid', 'avg', 'std', 'min', 'max',
                    'best_ind_length', 'avg_length', 'best_ind_nodes', 
                    'avg_nodes', 'best_ind_depth', 'avg_depth', 
                    'avg_used_codons', 'best_ind_used_codons', 
                    'structural_diversity', 'selection_time', 
                    'generation_time']
    
    start_time = time.time()

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
                                                            points_train=([X_train, y_train], 
                                                                          compiler, 
                                                                          n_registers),
                                                            codon_consumption=codon_consumption,
                                                            report_items=report_items,
                                                            genome_representation=genome_representation,
                                                            stats=stats,
                                                            halloffame=hof,
                                                            verbose=False)
    
    duration = time.time() - start_time

    display_best(hof)

    if output_path:
        record_results(output_path, run, report_items, ngen, logbook)
        save_run_info(output_path, run, hof, duration)

    return hof.items[0]


def multiple_runs(X_train, y_train, problem, compiler, n_registers, pop_size, 
                  ngen, cxpb, mutpb, elite_size, hof_size, tournsize, 
                  max_init_depth, min_init_depth, max_tree_depth, n_runs=30, 
                  output_path=None):

    """Runs the main flow of the GE algorithm multiple times.

    # Arguments
        X_train: A NumPy array containing training features.
        y_train: A NumPy array containing expected training classes.
        problem: A string indicating the problem.
        compiler: A string indicating the compiler to use.
        n_registers: Number of registers as an integer.
        pop_size: Population size as an integer.
        ngen: Number of generations as an integer.
        cxpb: Probability of crossover as a float.
        mutpb: Probability of mutation as a float.
        elite_size: Elite size as an integer.
        hof_size: Hall-of-fame size as an integer.
        tournsize: Tournament size as an integer.
        max_init_depth: Maximum initial depth as an integer.
        min_init_depth: Minimum initial depth as an integer.
        max_tree_depth: Maximum tree depth as an integer.
        n_run: Number of runs to execute as an integer.
        output_path: A string containing the path for the output directory or 
            None.

    # Returns
        None.
    """
    
    for run in range(n_runs):
        print(f"\nRun: {run}\n")

        np.random.seed(run)
        random.seed(run)

        run_algorithm(X_train, y_train, problem, compiler, n_registers, 
                      pop_size, ngen, cxpb, mutpb, elite_size, hof_size, 
                      tournsize, max_init_depth, min_init_depth, 
                      max_tree_depth, run, output_path)


def predict(X, expression, problem, compiler, n_registers):
    """Runs the main flow of the GE algorithm multiple times.

    # Arguments
        X: A NumPy array containing input features.
        expression: A string containing the code expression for an individual.
        compiler: A string indicating the compiler to use.
        n_registers: Number of registers as an integer.

    # Returns
        None.
    """
    if problem == 'drive':
        n_registers += 1
    
    pred = codegen.run_program(X, [expression], compiler, n_registers)[0]
    return [0 if pred[i] < 0.5 else 1 for i in range(len(pred))]


def main():
    timestamp = datetime.now().replace(microsecond=0).isoformat().replace(':', '')

    params = {
        "problem": "drive",
        "compiler": "gcc",
        "n_registers": 8,
        "pop_size": 100,
        "ngen": 1000,
        "cxpb": 0.6,
        "mutpb": 0.030339818402497533,
        "elite_size": 5,
        "hof_size": 7,
        "tournsize": 3,
        "max_init_depth": 12,
        "min_init_depth": 7,
        "max_tree_depth": 69
    }
    
    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--input")
    parser.add_argument("-o", "--output", default=timestamp)
    parser.add_argument("--problem")
    parser.add_argument("--compiler")
    parser.add_argument("--n_registers", type=int)
    parser.add_argument("--pop_size", type=int)
    parser.add_argument("--ngen", type=int)
    parser.add_argument("--cxpb", type=float)
    parser.add_argument("--mutpb", type=float)
    parser.add_argument("--elite_size", type=int)
    parser.add_argument("--hof_size", type=int)
    parser.add_argument("--tournsize", type=int)
    parser.add_argument("--max_init_depth", type=int)
    parser.add_argument("--min_init_depth", type=int)
    parser.add_argument("--max_tree_depth", type=int)
    parser.add_argument("--n_samples", type=int)

    kwargs = dict(parser.parse_args()._get_kwargs())

    output_path = os.path.join('results', kwargs['output'])
    os.makedirs(output_path, exist_ok=True)

    if kwargs['input']:
        with open(kwargs['input']) as jsonfile:
            json_data = json.load(jsonfile)
            params = json_data['params']
    
    for key in params.keys():
        if kwargs[key]:
            params[key] = kwargs[key]
    
    X_train, y_train, _, _ = set_dataset(params['problem'], n_samples=kwargs['n_samples'])

    with open(os.path.join(output_path, "params.json"), "w") as jsonfile:
        json.dump({'params': params}, jsonfile, indent=4)

    multiple_runs(X_train, y_train, **params, output_path=output_path)


if __name__ == "__main__":
    main()