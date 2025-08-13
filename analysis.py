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
import datetime
from tqdm import tqdm

from sklearn.metrics import accuracy_score, f1_score, classification_report, ConfusionMatrixDisplay

def read_csv_results(directory):
    roots = [os.path.splitext(f)[0] for f in os.listdir(directory) if f.endswith(".csv")]
    roots.sort(key=int)
    return [pd.read_csv(os.path.join(directory, f'{r}.csv'), sep='\t') for r in roots]


def read_json_results(directory):
    roots = [os.path.splitext(f)[0] for f in os.listdir(directory) if f.endswith(".json") and not f == 'params.json']
    roots.sort(key=int)
    
    best_inds = []
    execution_times = []

    for r in roots:
        with open(os.path.join(directory, f'{r}.json')) as jsonfile:
            json_data = json.load(jsonfile)
            best_inds.append(json_data['best_ind'])
            execution_times.append(json_data['execution_time'])
    
    return best_inds, execution_times


def plot_fitness(results, output_path):
    """Plots fitness statistics.

    Args:
        results:
    """

    colors = mpl.colormaps['Paired'].colors

    gen = results['gen']
    mean_fitness_values = results['avg']
    std_fitness_values = results['std']
    min_fitness_values = results['min']

    plt.errorbar(gen, mean_fitness_values, yerr=std_fitness_values, color=colors[3], label="Average")
    plt.plot(min_fitness_values, color=colors[5], label='Best individual')
    plt.legend()
    plt.xlabel('Generation')
    plt.ylabel('Fitness')
    plt.title('Fitness over Generations')
    plt.savefig(os.path.join(output_path, 'fitness.png'), dpi=300)
    plt.clf()


def plot_genome_length(results, output_path):
    """Plots genome length statistics.

    Args:
        results:
    """

    colors = mpl.colormaps['Paired'].colors

    best_ind_length = results['best_ind_length']
    avg_length = results['avg_length']

    plt.plot(avg_length, color=colors[1], label="Average")
    plt.plot(best_ind_length, color=colors[3], label="Best individual")
    plt.legend()
    plt.xlabel('Generation')
    plt.ylabel('Genome Length')
    plt.title('Genome Length over Generations')
    plt.savefig(os.path.join(output_path, 'genome_length.png'), dpi=300)
    plt.clf()


def plot_confusion_matrix(y_true, y_pred, output_path):
    ConfusionMatrixDisplay.from_predictions(y_true, y_pred, labels=[0, 1], values_format=',d',cmap='Blues')
    cb = plt.gca().images[-1].colorbar
    cb.ax.set_yticklabels([f"{tick:,.0f}" for tick in cb.get_ticks()])
    plt.title('Confusion Matrix')
    plt.savefig(os.path.join(output_path, 'confusion_matrix.png'), dpi=300)
    plt.clf()


def visualise_spiral(expression, params, output_path):
    colors = mpl.colormaps['Paired'].colors

    X, y = datasets.spiral_generate()

    X_grid = np.mgrid[X[:,0].min() - 0.5:X[:,0].max() + 0.5:200j, X[:,1].min() - 0.5:X[:,1].max() + 0.5:200j].reshape(2,-1).T
    y_grid_class = ge.predict(X_grid, expression, params['compiler'], params['n_registers'])

    plt.scatter(X_grid[:,0], X_grid[:,1], c=y_grid_class, s=1, marker=',', cmap=mpl.colors.ListedColormap([colors[0], colors[2]]))
    data = plt.scatter(X[:,0], X[:,1], c=y, cmap=mpl.colors.ListedColormap([colors[1], colors[3]]))

    plt.xlabel("$x$")
    plt.ylabel("$y$")
    plt.title("Decision Boundary")
    plt.legend(data.legend_elements()[0], [0, 1])

    ax = plt.gca()
    ax.set_aspect(aspect="equal")
    plt.savefig(os.path.join(output_path, 'decision_boundary.png'), dpi=300)
    plt.clf()


def visualise_drive(expression, params, output_path):
    image, manual, mask, X_sample = datasets.drive_get_sample_image()
    y_sample_class = ge.predict(X_sample, expression, params['problem'], params['compiler'], params['n_registers'])
    annotation = datasets.drive_annotate_sample_image(mask, y_sample_class)

    Image.fromarray(image).save(os.path.join(output_path, 'sample_image.gif'))
    Image.fromarray(manual).save(os.path.join(output_path, 'sample_manual.gif'))
    Image.fromarray(mask).save(os.path.join(output_path, 'sample_mask.gif'))
    Image.fromarray(annotation).save(os.path.join(output_path, 'sample_annotation.gif'))


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--input", required=True)

    kwargs = dict(parser.parse_args()._get_kwargs())

    with open(os.path.join(kwargs['input'], 'params.json')) as jsonfile:
        json_data = json.load(jsonfile)
        params = json_data['params']

    csv_results = read_csv_results(kwargs['input'])
    json_results = read_json_results(kwargs['input'])

    best_train_fitnesses = [r['min'].min() for r in csv_results]

    best_inds, execution_times = json_results
    best_expressions = [ge.evaluate_expression(r['phenotype']) for r in best_inds]
    
    _, _, X_test, y_test = ge.set_dataset(params['problem'])

    predictions = []
    accuracies = []
    f1_scores = []

    for expression in tqdm(best_expressions):
        y_class = ge.predict(X_test, expression, params['problem'], params['compiler'], params['n_registers'])
        
        predictions.append(y_class)
        accuracies.append(accuracy_score(y_test, y_class))
        f1_scores.append(f1_score(y_test, y_class))

    mean_train_fitness = np.mean(best_train_fitnesses)
    std_train_fitness = np.std(best_train_fitnesses)
    mean_test_accuracy = np.mean(accuracies)
    std_test_accuracy = np.std(accuracies)
    mean_test_f1_score = np.mean(f1_scores)
    std_test_f1_score = np.std(f1_scores)
    mean_execution_time = np.mean(execution_times)

    print(f"Average results over {len(csv_results)} runs after {len(csv_results[0]) - 1} generations.")
    print(f"Training fitness: {mean_train_fitness:.4f} (standard deviation: {std_train_fitness:.4f})")
    print(f"Test accuracy: {mean_test_accuracy:.4f} (standard deviation: {std_test_accuracy:.4f})")
    print(f"Test f1-score: {mean_test_f1_score:.4f} (standard deviation: {std_test_f1_score:.4f})")
    print(f"Execution time: {datetime.timedelta(seconds=mean_execution_time)}\n")

    best_run = np.argmax(f1_scores)
    best_run_expression = best_expressions[best_run]
    best_run_prediction = predictions[best_run]
    best_run_individual = best_inds[best_run]

    print("Best individual:\n" + best_run_expression + "\n")
    print("Training fitness:", best_run_individual['fitness'])
    print("Depth:", best_run_individual['depth'])
    print("Length of the genome:", len(best_run_individual['genome']))
    print(f"Used portion of the genome: {best_run_individual['used_codons'] / len(best_run_individual['genome']):.4f}\n")
    
    print(classification_report(y_test, best_run_prediction, digits=4))
    
    output_path = os.path.join('visualisations', params['problem'], params['compiler'])
    os.makedirs(output_path, exist_ok=True)

    plot_fitness(csv_results[best_run], output_path)
    plot_genome_length(csv_results[best_run], output_path)
    plot_confusion_matrix(y_test, best_run_prediction, output_path)

    if params['problem'] == 'spiral':
        visualise_spiral(best_run_expression, params, output_path)
    elif params['problem'] == 'drive':
        visualise_drive(best_run_expression, params, output_path)


if __name__ == "__main__":
    main()