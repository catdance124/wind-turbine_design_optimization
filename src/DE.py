import os, random
import numpy as np
# my modules
from setting import *
from file_handler import write_vars, read_objs, read_cons

def initialize():
    

def evaluate(trial_individual):
    # 解候補出力
    write_vars(trial_individual)
    # 評価モジュール実行
    os.system('evaluation.bat')
    # 結果受け取り＆score算出
    objs = read_objs()
    cons = read_cons()
    score = objs + cons*10000
    return score

def main():
    # init
    trial_individual = [0] * D
    current_gen = np.random.uniform(0, 1, (NP, D))
    next_gen = current_gen.copy()
    cost = np.full(NP, 10e+10)

    # generation loop
    for gen_count in range(1, GEN_MAX + 1):
        for NP_i in range(NP):
            """ 突然変異・交叉 """
            # a,b,c 3個体を選択する (a!=b!=c!=NP_i)
            indices = list(range(NP))
            indices.pop(NP_i)
            a, b, c = random.sample(indices, 3)
            
            # trial個体を作成
            D_i = random.choice(list(range(D)))
            for k in range(1, D+1):
                if (random.uniform(0, 1) < CR) or (k == D):
                    trial_individual[D_i] = current_gen[c][D_i] + F*(current_gen[a][D_i] - current_gen[b][D_i])
                else:
                    trial_individual[D_i] = current_gen[NP_i][D_i]
                D_i = (D_i + 1) % D
			
            """ 評価 """
            score = 100#evaluate(trial_individual)
            print(score)

            """ 選択 """
            if score <= cost[NP_i]:    # update
                next_gen[NP_i] = trial_individual
                cost[NP_i] = score
            else:                      # non update
                next_gen[NP_i] = current_gen[NP_i]
        
        """ 世代交代 """
        current_gen = next_gen
        print(gen_count, min(cost))


if __name__ == "__main__":
    main()
    read_objs()
    read_cons()