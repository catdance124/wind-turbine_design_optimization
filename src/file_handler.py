import os
import csv
import datetime
import numpy as np
# my modules
from setting import *

file_dir = '../evaluation'
start = datetime.datetime.now()
logs_dir = '../logs'
os.makedirs(logs_dir, exist_ok=True)

def write_vars(trial_individuals):
    with open(f'{file_dir}/pop_vars_eval.txt', 'w', newline='') as f:
        writer = csv.writer(f, delimiter='\t')
        for trial_individual in trial_individuals:
            writer.writerow(trial_individual)

def read_objs():
    with open(f'{file_dir}/pop_objs_eval.txt', 'r') as f:
        reader = csv.reader(f)
        objs = [row for row in reader]
        objs = [[float(v) for v in row] for row in objs]
    return np.array(objs).reshape((-1,))

def read_cons():
    with open(f'{file_dir}/pop_cons_eval.txt', 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        cons = [row for row in reader]
        cons = [[float(v) for v in row] for row in cons]
    return np.array(cons)

def write_logs(gen_count, score, minus, best_individual):
    with open(f'{logs_dir}/{start.strftime("%m-%d %H_%M_%S")}_NP{NP}_CR{CR}_F{F}.csv', 'a', newline="") as f:
        writer = csv.writer(f)
        if gen_count==1:
            # writer.writerow([f'NP:{NP}', f'CR:{CR}', f'F:{F}'])
            writer.writerow(['gen', 'score', 'minus', *list(range(1,33))])
        writer.writerow([f'{gen_count:03}', score, minus, *best_individual])

# def convert_vars(individual):
#     # スケール変換
#     for i, x in enumerate(individual):
#         individual[i] = (x - LOWER[i]) / (UPPER[i] - LOWER[i])
#     return individual

# def convert_vars(individual):
#     ind_min = min(individual)
#     ind_max = max(individual)
#     return [float(i - ind_min) / (ind_max - ind_min) for i in individual]