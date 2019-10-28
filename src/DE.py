import os, random
import numpy as np
# my modules
from setting import *
from file_handler import write_vars, read_objs, read_cons, write_logs


def evaluate(trial_individuals):
    # 解候補出力
    write_vars(trial_individuals)
    # 評価モジュール実行
    os.system('evaluation.bat')
    # 結果受け取り
    objs = read_objs()
    cons = read_cons()
    # スコア算出
    #errors_n = np.sum(cons<0, axis=1)
    errors_n = (-1)*np.sum(cons[cons<0])
    scores = objs + errors_n*100
    return scores

def main():
    # init
    trial_individuals = np.zeros((NP,D))
    current_gen = np.random.uniform(0, 1, (NP, D))
    for D_i in range(D):
        current_gen[:, D_i] = np.random.uniform(LOWER[D_i], UPPER[D_i], NP)
    next_gen = current_gen.copy()
    
    # first evaluation
    scores = evaluate(current_gen)
    best = np.argmin(scores)
    print(f'gen:1, score:{scores[best]}')
    write_logs(1, scores[best], current_gen[best])
    
    # generation loop
    for gen_count in range(2, GEN_MAX + 1):
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
                    trial_individuals[NP_i, D_i] = current_gen[c, D_i] + F*(current_gen[a, D_i] - current_gen[b, D_i])
                else:
                    trial_individuals[NP_i, D_i] = current_gen[NP_i, D_i]
                D_i = (D_i + 1) % D
        
        """ 評価 """
        trial_scores = evaluate(trial_individuals)

        """ 選択 """
        update_index = trial_scores <= scores
        print(trial_scores)
        print(scores)
        print(update_index)
        # update
        next_gen[update_index] = trial_individuals[update_index]
        scores[update_index] = trial_scores[update_index]
        # npn update
        next_gen[~update_index] = current_gen[~update_index]

        """ 世代交代 """
        current_gen = next_gen
        
        # 出力処理
        best = np.argmin(scores)
        print(f'gen:{gen_count}, score:{scores[best]}')
        write_logs(gen_count, scores[best], current_gen[best])


if __name__ == "__main__":
    main()