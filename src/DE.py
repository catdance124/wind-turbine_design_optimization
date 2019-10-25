import random

gen_max = 200
NP = 5  # 個体数
D = 3    # 設計変数の数
CR = 0.1 # 交叉定数
F = 0.9  # スケーリングファクタ

def evaluate(trial):    # sphere func
    value = 0
    for D_i in trial:
        value += D_i * D_i
    return value


def main():
    trial_individual = [0] * D
    current_gen = [[(random.uniform(0, 1)*2-1)*5.12] * D for i in range(NP)]
    next_gen = current_gen
    cost = [10e+10] * NP

    for gen_count in range(1, gen_max + 1):
        for NP_i in range(NP):
            """ 突然変異・交叉 """
            # a,b,c 3個体を選択する (a!=b!=c!=NP_i)
            indices = list(range(NP))
            indices.pop(NP_i)
            a, b, c = random.sample(indices, 3)
            
            # 説明変数ごとで交叉しtrial個体を作成
            D_i = random.choice(list(range(D)))
            for k in range(1, D+1):
                if (random.uniform(0, 1) < CR) or (k == D):
                    trial_individual[D_i] = current_gen[c][D_i] + F*(current_gen[a][D_i] - current_gen[b][D_i])
                else:
                    trial_individual[D_i] = current_gen[NP_i][D_i]
                D_i = (D_i + 1) % D
            
            """ 評価 """
            score = evaluate(trial_individual)

            """ 選択 """
            if score <= cost[NP_i]:    # update
                for D_i in range(D):
                    next_gen[NP_i][D_i] = trial_individual[D_i]
                cost[NP_i] = score
            else:                      # non update
                for D_i in range(D):
                    next_gen[NP_i][D_i] = current_gen[NP_i][D_i]
        
        """ 世代交代 """
        current_gen = next_gen
        print(gen_count, min(cost))

if __name__ == "__main__":
    main()