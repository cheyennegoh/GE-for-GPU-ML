import ge

from sklearn.base import BaseEstimator, ClassifierMixin
from skopt import BayesSearchCV
from skopt.space import Real, Integer


class GrammaticalEvolution(BaseEstimator, ClassifierMixin):
    def __init__(self, bnf_grammar, pop_size, ngen, cxpb=0.8, mutpb=0.1, 
                 elite_size=5, hof_size=5, tournsize=5, max_init_depth=13, 
                 min_init_depth=5, max_tree_depth=35):
        
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
        self.elite_size = min(self.elite_size, self.hof_size)
        self.max_init_depth = max(self.max_init_depth, self.min_init_depth)
        self.max_tree_depth = max(self.max_tree_depth, self.max_init_depth)

        params = {"pop_size": self.pop_size,
                  "ngen": self.ngen,
                  "cxpb": self.cxpb,
                  "mutpb": self.mutpb,
                  "elite_size": self.elite_size,
                  "hof_size": self.hof_size,
                  "tournsize": self.tournsize,
                  "max_init_depth": self.max_init_depth,
                  "min_init_depth": self.min_init_depth,
                  "max_tree_depth": self.max_tree_depth}
        
        print(f'\n{params}\n')

        self.best_individual = ge.run_algorithm(X, y, self.bnf_grammar,
                                                self.pop_size, self.ngen,
                                                self.cxpb, self.mutpb,
                                                self.elite_size, self.hof_size,
                                                self.tournsize,
                                                self.max_init_depth,
                                                self.min_init_depth,
                                                self.max_tree_depth)
        
        self.model = self

        return self


    def predict(self, X):
        pred = ge.run_c_program(X, [ge.evaluate_expression(self.best_individual.phenotype)])[0]
        return [1 if pred[i] > 0 else 0 for i in range(len(pred))]
    

    def score(self, X, y):
        return 1 - ge.fitness_eval([self.best_individual], [X, y], False)[0]


X, y, bnf_grammar = ge.setDataSet(test_size=0)

optGE = BayesSearchCV(
    estimator=GrammaticalEvolution(bnf_grammar=bnf_grammar,
                                   pop_size=100,
                                   ngen=100),
    search_spaces={
        'cxpb': Real(1e-3, 1, prior='log-uniform'),
        'mutpb': Real(1e-3, 1, prior='log-uniform'),
        'elite_size': Integer(0, 10), # min must be 0
        'hof_size': Integer(1, 10), # min must be 1
        'tournsize': Integer(2, 7),
        'max_init_depth': Integer(6, 14), # max must be 14
        'min_init_depth': Integer(5, 7), # min must be 5
        'max_tree_depth': Integer(25, 45)
    },
    n_iter=40,
    cv=3,
    verbose=2,
)

optGE.fit(X, y)

print(f"Validation accuracy: {optGE.best_score_}")
print(f"Accuracy: {optGE.score(X, y)}")
print("Best parameters: ", end='')
print(*[f"{key}={value}" for key, value in optGE.best_params_.items()], sep=', ', end='\n\n')
