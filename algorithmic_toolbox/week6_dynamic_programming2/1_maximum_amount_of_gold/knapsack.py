# Uses python3
from pprint import pprint


def optimal_weight(W, w):
    n = len(w)
    w = [0] + w
    value = [[0] * (W + 1) for x in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, W + 1):
            value[i][j] = value[i - 1][j]
            if w[i] <= j:
                val = value[i - 1][j - w[i]] + w[i]
                value[i][j] = max(val, value[i][j])
    return value[n][W]


W, _ = [int(x) for x in input().split()]
w = [int(x) for x in input().split()]
print(optimal_weight(W, w))
