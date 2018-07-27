#Uses python3


def max_dot_product(a, b):
    a.sort()
    b.sort()
    res = sum([x * y for x, y in zip(a, b)])
    return res

    
n = int(input())
profit_per_clicks = [int(x) for x in input().split()]
ave_clicks = [int(x) for x in input().split()]
print(max_dot_product(profit_per_clicks, ave_clicks))
