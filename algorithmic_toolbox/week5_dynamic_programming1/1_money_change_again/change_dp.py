# Uses python3


def get_change(m, coins):
    moneys = [0] + [float('inf')] * m
    for i in range(1, m+1):
        for coin in coins:
            if i >= coin and moneys[i] > moneys[i - coin] + 1:
                moneys[i] = moneys[i - coin] + 1
    return moneys[-1]


m = int(input())
coins = [1, 3, 4]
print(get_change(m, coins))
