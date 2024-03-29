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
    minus = np.sum(cons<0, axis=1)
    # errors_n = (-1)*np.sum(cons[cons<0])
    scores = objs + minus * 10e+8
    return scores, minus

def main():
    # init
    trial_individuals = np.zeros((NP,D))
    current_gen = np.random.uniform(0, 1, (NP, D))
    next_gen = current_gen.copy()
    
    # first evaluation
    scores, minus = evaluate(current_gen)
    best = np.argmin(scores)
    print(f'gen:1, score:{scores[best]}, minus:{minus[best]}')
    write_logs(1, scores[best], minus[best], current_gen[best])
    
    # generation loop
    for gen_count in range(2, GEN_MAX + 1):
        for NP_i in range(NP):
            """ 突然変異・交叉 """
            # a,b,c 3個体を選択する (a!=b!=c!=NP_i)
            indices = list(range(NP))
            indices.pop(NP_i)
            a, b, c = random.sample(indices, 3)
            # best個体の設計変数を取り入れる
            # if best !=NP_i:
            #     c = best
            
            # trial個体を作成
            D_i = random.choice(list(range(D)))
            for k in range(1, D+1):
                if (random.uniform(0, 1) < CR) or (k == D):
                    M = F*(current_gen[a, D_i] - current_gen[b, D_i])
                    C = current_gen[c, D_i]
                    trial_individuals[NP_i, D_i] = C + M
                    if trial_individuals[NP_i, D_i] < 0:
                        trial_individuals[NP_i, D_i] = - (C + M)
                    elif 1 < trial_individuals[NP_i, D_i]:
                        trial_individuals[NP_i, D_i] = 2 - (C + M)
                else:
                    trial_individuals[NP_i, D_i] = current_gen[NP_i, D_i]
                D_i = (D_i + 1) % D
        
        """ 評価 """
        trial_scores, trial_minus = evaluate(trial_individuals)

        """ 選択 """
        update_index = trial_scores <= scores
        print(trial_scores)
        print(scores)
        print(update_index)
        # update
        next_gen[update_index] = trial_individuals[update_index]
        scores[update_index] = trial_scores[update_index]
        minus[update_index] = trial_minus[update_index]
        # non update
        next_gen[~update_index] = current_gen[~update_index]

        """ 世代交代 """
        current_gen = next_gen
        
        # 出力処理
        best = np.argmin(scores)
        print(f'gen:{gen_count}, score:{scores[best]}, minus:{minus[best]}')
        write_logs(gen_count, scores[best], minus[best], current_gen[best])


if __name__ == "__main__":
    main()