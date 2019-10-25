import csv

file_dir = '../evaluation'

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
        # print(score)
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