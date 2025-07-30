# analysis.py

import os
import argparse

import numpy as np
import pandas as pd


def read_results(directory):
    roots = [os.path.splitext(f)[0] for f in os.listdir(directory) if f.endswith(".csv")]
    roots.sort(key=int)
    return [pd.read_csv(os.path.join(directory, f'{r}.csv'), sep='\t') for r in roots]


def avg_best_fitness(results):
    best_fitnesses = [r['min'].min() for r in results]

    mean = np.mean(best_fitnesses)
    std = np.std(best_fitnesses)

    return mean, std


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--input", required=True)

    kwargs = dict(parser.parse_args()._get_kwargs())

    results = read_results(kwargs['inputs'])
    mean, std = avg_best_fitness(results)

    print(f"Average results over {len(results)} runs after {len(results[0]) - 1} generations.")
    print("Mean:", mean)
    print("Standard deviation:", std)


if __name__ == "__main__":
    main()