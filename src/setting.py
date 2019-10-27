NP = 10    # 個体数
D = 32     # 設計変数の数
C = 22     # 制約条件の数

GEN_MAX = 10000//NP  # 世代上限
CR = 0.1   # 交叉定数
F = 0.9    # スケーリングファクタ


# 各設計変数の下限
LOWER = [1.0, 1.0, 1.0, 1.0, 0.1, -5, -5, -5, -5, \
    0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, \
        -6.3, -6.3, -6.3, 6.0, 6.0, 50, 20, 3.87, 3.87, 3.87, 0.005, 0.005, 0.005]
# 各設計変数の上限
UPPER = [5.3, 5.3, 5.3, 5.3, 0.3, 30, 30, 30, 30, \
    0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, \
        0.0, 0.0, 0.0, 14.0, 20.0, 80, 70, 6.3, 6.3, 6.3, 0.1, 0.1, 0.1]