import os
import csv
import datetime
from setting import *

file_dir = '../evaluation'
start = datetime.datetime.now()
logs_dir = '../logs'
os.makedirs(logs_dir, exist_ok=True)

def write_vars(trial_individual):
    with open(f'{file_dir}/pop_vars_eval.txt', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow(trial_individual)

def read_objs():
    with open(f'{file_dir}/pop_objs_eval.txt', 'r') as f:
        reader = csv.reader(f)
        l = [row for row in reader]
        l = [[float(v) for v in row] for row in l]
        score = l[0][0]
    return score

def read_cons():
    error_count = 0
    with open(f'{file_dir}/pop_cons_eval.txt', 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        l = [row for row in reader]
        l = [[float(v) for v in row] for row in l]
        for con in l[0]:
            if con < 0:
                error_count += 1
    return error_count

def write_logs(gen_count, score, raw_score, minus, best_individual):
    with open(f'{logs_dir}/{start.strftime("%m-%d %H_%M_%S")}.csv', 'a', newline="") as f:
        writer = csv.writer(f)
        if gen_count==2:
            writer.writerow([f'NP:{NP}', f'CR:{CR}', f'F:{F}'])
            writer.writerow(['gen', 'score', 'raw score', 'minus', *list(range(1,33))])
        writer.writerow([f'{gen_count:03}', score, raw_score, minus, *convert_vars(best_individual)])

def convert_vars(individual):
    # 各設計変数の下限
    LOWER = [1.0, 1.0, 1.0, 1.0, 0.1, -5, -5, -5, -5, \
        0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, \
            -6.3, -6.3, -6.3, 6.0, 6.0, 50, 20, 3.87, 3.87, 3.87, 0.005, 0.005, 0.005]
    # 各設計変数の上限
    UPPER = [5.3, 5.3, 5.3, 5.3, 0.3, 30, 30, 30, 30, \
        0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, \
            0.0, 0.0, 0.0, 14.0, 20.0, 80, 70, 6.3, 6.3, 6.3, 0.1, 0.1, 0.1]
    # スケール変換
    for i, x in enumerate(individual):
        individual[i] = x * (UPPER[i] - LOWER[i]) + LOWER[i]
    return individual