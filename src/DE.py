import os, random
import numpy as np
# my modules
from setting import *
from file_handler import write_vars, read_objs, read_cons, write_logs


def evaluate(trial_individual):
    # 解候補出力
    write_vars(trial_individual)
    # 評価モジュール実行
    os.system('evaluation.bat')
    # 結果受け取り
    return read_objs(), read_cons()

def main():
    # init
    trial_individual = [0] * D
    current_gen = np.random.uniform(0, 1, (NP, D))
    next_gen = current_gen.copy()
    score = np.full(NP, 10e+10)
    minus = np.full(NP, 10e+10)
    raw_score = np.full(NP, 10e+10)
    
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
                    trial_individual[D_i] = current_gen[c][D_i] + F*(current_gen[a][D_i] - current_gen[b][D_i])
                else:
                    trial_individual[D_i] = current_gen[NP_i][D_i]
                D_i = (D_i + 1) % D
			
            """ 評価 """
            objs, cons = evaluate(trial_individual)
            trial_score = objs + cons*100

            """ 選択 """
            if trial_score <= score[NP_i]:    # update
                next_gen[NP_i] = trial_individual
                score[NP_i] = trial_score
                raw_score[NP_i] = objs
                minus[NP_i] = cons
            else:                      # non update
                next_gen[NP_i] = current_gen[NP_i]
            # print(score[NP_i])
        """ 世代交代 """
        current_gen = next_gen
        
        # 出力処理
        best = np.argmin(score)
        print(f'gen:{gen_count}, score:{score[best]}, raw:{raw_score[best]}, minus:{minus[best]}')
        write_logs(gen_count, score[best], raw_score[best], minus[best], current_gen[best])


if __name__ == "__main__":
    main()