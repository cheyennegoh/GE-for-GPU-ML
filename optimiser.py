import ge

from sklearn.base import BaseEstimator, ClassifierMixin
from skopt import BayesSearchCV
from skopt.space import Real, Integer

from pathlib import Path
from datetime import datetime
import json


class GrammaticalEvolution(BaseEstimator, ClassifierMixin):
    def __init__(self, bnf_grammar, pop_size, ngen, cxpb=0.970086292848572, mutpb=0.19412625414340878, 
                 elite_size=5, hof_size=5, tournsize=4, max_init_depth=14, 
                 min_init_depth=6, max_tree_depth=26):
        
        self.bnf_grammar = bnf_grammar
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

        self.best_individual = ge.run_algorithm(X, y, self.bnf_grammar, **params)
        self.model = self
        return self


    def predict(self, X):
        pred = ge.run_c_program(X, [ge.evaluate_expression(self.best_individual.phenotype)])[0]
        return [1 if pred[i] > 0 else 0 for i in range(len(pred))]
    

    def score(self, X, y):
        return 1 - ge.fitness_eval([self.best_individual], [X, y], False)[0]


    @staticmethod
    def constrain_params(params):
        keys = ["pop_size", "ngen", "cxpb", "mutpb", "elite_size", "hof_size", 
                "tournsize", "max_init_depth", "min_init_depth", 
                "max_tree_depth"]
        
        params = {key: params[key] for key in keys if key in params}

        params['elite_size'] = min(params['elite_size'], params['hof_size'])
        params['max_init_depth'] = max(params['max_init_depth'], params['min_init_depth'])
        params['max_tree_depth'] = max(params['max_tree_depth'], params['max_init_depth'])

        return params


def main():
    X, y, bnf_grammar = ge.setDataSet(test_size=0)

    optGE = BayesSearchCV(
        estimator=GrammaticalEvolution(bnf_grammar=bnf_grammar,
                                    pop_size=10,
                                    ngen=10),
        search_spaces={
            'cxpb': Real(0.8, 1, prior='log-uniform'),
            'mutpb': Real(0.03, 0.3, prior='log-uniform'),
            'elite_size': Integer(6, 8), # min must be >0
            'hof_size': Integer(3, 5), # min must be >1
            'tournsize': Integer(3, 5),
            'max_init_depth': Integer(13, 14), # max must be <14
            'min_init_depth': Integer(5, 7), # min must be >5
            'max_tree_depth': Integer(25, 27)
        },
        n_iter=1,
        cv=2,
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