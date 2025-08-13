# optimiser.py

import ge

from sklearn.base import BaseEstimator, ClassifierMixin
from skopt import BayesSearchCV
from skopt.space import Real, Integer, Categorical

import os
from datetime import datetime
import json
import argparse

class GrammaticalEvolution(BaseEstimator, ClassifierMixin):
    def __init__(self, problem='drive', compiler='gcc', n_registers=8, 
                 pop_size=100, ngen=1000, cxpb=0.6, mutpb=0.030339818402497533,
                 elite_size=5, hof_size=7, tournsize=3, max_init_depth=12, 
                 min_init_depth=7, max_tree_depth=69):
        
        self.problem = problem
        self.compiler = compiler
        self.n_registers = n_registers
        self.pop_size = pop_size
        self.ngen = ngen
        self.cxpb = cxpb
        self.mutpb = mutpb
        self.elite_size = elite_size
        self.hof_size = hof_size
        self.tournsize = tournsize
        self.max_init_depth = max_init_depth
        self.min_init_depth = min_init_depth
        self.max_tree_depth = max_tree_depth


    def fit(self, X, y):
        params = self.constrain_params(vars(self))
        print(f'\nParams: {params}\n')

        self.best_individual = ge.run_algorithm(X, y, **params)
        self.model = self
        return self


    def predict(self, X):
        return ge.predict(X, 
                          ge.evaluate_expression(self.best_individual.phenotype),
                          self.problem,
                          self.compiler,
                          self.n_registers)
    

    def score(self, X, y):
        return 1 - ge.fitness_eval([self.best_individual], 
                                   ([X, y], 
                                    self.compiler, 
                                    self.n_registers + 1 if self.problem == 'drive' else self.n_registers), 
                                   False)[0]


    @staticmethod
    def constrain_params(params, n_evals=100000):
        keys = ['problem', 'compiler', 'n_registers', 'pop_size', 'ngen', 
                'cxpb', 'mutpb', 'elite_size', 'hof_size', 'tournsize', 
                'max_init_depth', 'min_init_depth', 'max_tree_depth']
        
        params = {key: params[key] for key in keys if key in params}

        if n_evals:
            params['ngen'] = n_evals // params['pop_size']
        
        params['elite_size'] = min(params['elite_size'], params['hof_size'])
        params['max_init_depth'] = max(params['max_init_depth'], params['min_init_depth'])
        params['max_tree_depth'] = max(params['max_tree_depth'], params['max_init_depth'])

        return params


def main():
    timestamp = datetime.now().replace(microsecond=0).isoformat().replace(':', '')

    categorical = ['n_registers', 'pop_size']
    real = ['cxpb', 'mutpb']
    integer = ['elite_size', 'hof_size', 'tournsize', 'max_init_depth', 'min_init_depth','max_tree_depth']

    all_spaces = categorical + real + integer

    parser = argparse.ArgumentParser()

    parser.add_argument("-o", "--output", default=f'{timestamp}.json')
    parser.add_argument("--spaces", nargs='+', default=all_spaces)
    parser.add_argument("--problem", default='drive')
    parser.add_argument("--compiler", default='gcc')
    parser.add_argument("--n_registers", type=int, nargs='+', default=[6, 8, 10])
    parser.add_argument("--pop_size", type=int, nargs='+', default=[10, 100, 1000])
    parser.add_argument("--cxpb", type=float, nargs=2, default=[0.5, 0.7])
    parser.add_argument("--mutpb", type=float, nargs=2, default=[0.01, 0.1])
    parser.add_argument("--elite_size", type=int, nargs=2, default=[4, 6]) # min must be >= 0
    parser.add_argument("--hof_size", type=int, nargs=2, default=[6, 8]) # min must be >= 1
    parser.add_argument("--tournsize", type=int, nargs=2, default=[3, 5])
    parser.add_argument("--max_init_depth", type=int, nargs=2, default=[12, 14])
    parser.add_argument("--min_init_depth", type=int, nargs=2, default=[7, 9]) # min must be >= 4
    parser.add_argument("--max_tree_depth", type=int, nargs=2, default=[25, 75])
    parser.add_argument("--n_samples", type=int)

    kwargs = dict(parser.parse_args()._get_kwargs())

    search_spaces = {}
    for space in kwargs['spaces']:
        if space in categorical:
            search_spaces[space] = Categorical(kwargs[space], transform='identity')
        elif space in real:
            search_spaces[space] = Real(*kwargs[space], prior='log-uniform')
        elif space in integer:
            search_spaces[space] = Integer(*kwargs[space])
    
    X_train, y_train, _, _ = ge.set_dataset(kwargs['problem'], n_samples=kwargs['n_samples'])

    optGE = BayesSearchCV(
        estimator=GrammaticalEvolution(problem=kwargs['problem'],
                                       compiler=kwargs['compiler']),
        search_spaces=search_spaces,
        n_iter=30,
        cv=3,
        verbose=10
    )

    optGE.fit(X_train, y_train)

    results = {
        'val_acc': optGE.best_score_,
        'search_spaces': {key : value.bounds for key, value in search_spaces.items()},
        'params': GrammaticalEvolution.constrain_params(vars(optGE.best_estimator_))
    }

    os.makedirs('optimisation', exist_ok=True)

    with open(os.path.join('optimisation', kwargs['output']), "w") as jsonfile:
        json.dump(results, jsonfile, indent=4)


if __name__ == "__main__":
    main()