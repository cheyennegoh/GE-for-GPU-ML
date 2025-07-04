import ge
import codegen

from sklearn.base import BaseEstimator, ClassifierMixin
from skopt import BayesSearchCV
from skopt.space import Real, Integer, Categorical

from pathlib import Path
from datetime import datetime
import json


class GrammaticalEvolution(BaseEstimator, ClassifierMixin):
    def __init__(self, problem='spiral', compiler='gcc', n_registers=2, 
                 pop_size=100, ngen=1000, cxpb=0.9461505693738687, 
                 mutpb=0.209973308669768, elite_size=5, hof_size=5, 
                 tournsize=4, max_init_depth=13, min_init_depth=5, 
                 max_tree_depth=25):
        
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
        pred = codegen.run_program(X, 
                                   [ge.evaluate_expression(self.best_individual.phenotype)],
                                   self.compiler,
                                   self.n_registers)[0]
        return [1 if pred[i] > 0 else 0 for i in range(len(pred))]
    

    def score(self, X, y):
        return 1 - ge.fitness_eval([self.best_individual], 
                                   ([X, y], self.compiler, self.n_registers), 
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
    problem = 'spiral'
    
    X, y = ge.set_dataset(problem)

    optGE = BayesSearchCV(
        estimator=GrammaticalEvolution(problem=problem,
                                       compiler='gcc'),
        search_spaces={
            'n_registers': Categorical([2, 4, 6], transform='identity'),
            'pop_size': Categorical([10, 100, 1000], transform='identity'),
            'cxpb': Real(0.8, 1, prior='log-uniform'),
            'mutpb': Real(0.1, 0.3, prior='log-uniform'),
            # 'elite_size': Integer(6, 8), # min must be >0
            # 'hof_size': Integer(3, 5), # min must be >1
            # 'tournsize': Integer(3, 5),
            # 'max_init_depth': Integer(13, 14), # max must be <14
            # 'min_init_depth': Integer(5, 7), # min must be >5
            # 'max_tree_depth': Integer(25, 27)
        },
        n_iter=40,
        cv=5,
        verbose=10
    )

    optGE.fit(X, y)

    results = {
        'val_acc': optGE.best_score_,
        'params': GrammaticalEvolution.constrain_params(vars(optGE.best_estimator_))
    }

    Path(r"./optimisation/").mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().replace(microsecond=0).isoformat().replace(':', '')
    with open(r"./optimisation/" + timestamp + ".json", "w") as jsonfile:
        json.dump(results, jsonfile, indent=4)


if __name__ == "__main__":
    main()