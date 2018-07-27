# Uses python3


def optimal_summands(n):
    summands = []
    current_prize = 0
    while n > 0:
        current_prize += 1
        if current_prize <= n:
            summands.append(current_prize)
            n -= current_prize
        else:
            summands[-1] += n
            n = 0
    return summands


n = int(input())
summands = optimal_summands(n)
print(len(summands))
print(' '.join([str(x) for x in summands]))
