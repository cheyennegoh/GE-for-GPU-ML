# analysis.py

from PIL import Image

import matplotlib as mpl
import matplotlib.pyplot as plt

import ge
import datasets

import os
import argparse

import math
import numpy as np
import pandas as pd

import json

from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay

def read_csv_results(directory):
    roots = [os.path.splitext(f)[0] for f in os.listdir(directory) if f.endswith(".csv")]
    roots.sort(key=int)
    return [pd.read_csv(os.path.join(directory, f'{r}.csv'), sep='\t') for r in roots]


def read_json_results(directory):
    roots = [os.path.splitext(f)[0] for f in os.listdir(directory) if f.endswith(".json") and not f == 'params.json']
    roots.sort(key=int)
    
    results = []
    for r in roots:
        with open(os.path.join(directory, f'{r}.json')) as jsonfile:
            json_data = json.load(jsonfile)
            results.append(json_data['best_ind'])
    
    return results


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--input", required=True)
    # parser.add_argument("--n_samples", type=int)

    kwargs = dict(parser.parse_args()._get_kwargs())

    with open(os.path.join(kwargs['input'], 'params.json')) as jsonfile:
        json_data = json.load(jsonfile)
        params = json_data['params']

    csv_results = read_csv_results(kwargs['input'])
    json_results = read_json_results(kwargs['input'])

    best_train_fitnesses = [r['min'].min() for r in csv_results]

    mean = np.mean(best_train_fitnesses)
    std = np.std(best_train_fitnesses)

    print(f"Average results over {len(csv_results)} runs after {len(csv_results[0]) - 1} generations.")
    print("Mean:", mean)
    print("Standard deviation:", std)

    _, _, X_test, y_test = ge.set_dataset(params['problem'])

    best_expressions = [ge.evaluate_expression(r['phenotype']) for r in json_results]
    
    predictions = []
    accuracies = []

    for expression in best_expressions:
        y_class = ge.predict(X_test, expression, params['compiler'], params['n_registers'])

        accuracies.append(accuracy_score(y_test, y_class))
        predictions.append(y_class)
    
    best_run = np.argmax(accuracies)
    best_run_expression = best_expressions[best_run]
    best_run_prediction = predictions[best_run]
    
    print(classification_report(y_test, best_run_prediction))
    
    # Visualise results
    os.makedirs('visualisations', exist_ok=True)

    ConfusionMatrixDisplay.from_predictions(y_test, best_run_prediction)
    plt.savefig(os.path.join('visualisations', 'confusion-matrix.png'))
    plt.clf()

    if params['problem'] == 'drive':        
        image, manual, mask, X_sample = datasets.drive_sample_test_image()
        y_sample_class = ge.predict(X_sample, best_run_expression, params['compiler'], params['n_registers'])
        annotation = datasets.drive_annotate_sample_test_image(mask, y_sample_class)
    
        Image.fromarray(image).save(os.path.join('visualisations', 'sample_test_image.gif'))
        Image.fromarray(manual).save(os.path.join('visualisations', 'sample_test_manual.gif'))
        Image.fromarray(mask).save(os.path.join('visualisations', 'sample_test_mask.gif'))
        Image.fromarray(annotation).save(os.path.join('visualisations', 'sample_test_annotation.gif'))
    
    if params['problem'] == 'spiral':
        colors = mpl.colormaps['Paired'].colors

        X, y = datasets.spiral_generate()

        bound = 2 * math.pi
        X_grid = np.mgrid[X[:,0].min() - 0.5:X[:,0].max() + 0.5:200j, X[:,1].min() - 0.5:X[:,1].max() + 0.5:200j].reshape(2,-1).T
        y_grid_class = ge.predict(X_grid, best_run_expression, params['compiler'], params['n_registers'])

        plt.scatter(X_grid[:,0], X_grid[:,1], c=y_grid_class, s=1, marker=',', cmap=mpl.colors.ListedColormap([colors[0], colors[2]]))
        plt.scatter(X[:,0], X[:,1], c=y, cmap=mpl.colors.ListedColormap([colors[1], colors[3]]))

        ax = plt.gca()
        ax.set_aspect(aspect="equal")
        plt.savefig(os.path.join('visualisations', 'classification-threshold.png'))
        plt.clf()


if __name__ == "__main__":
    main()