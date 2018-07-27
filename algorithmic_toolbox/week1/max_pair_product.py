# Uses python3


def get_max(a):
    max1 = 0
    for ele in a:
        if ele > max1:
            max1 = ele
    return max1


n = int(input())
a = [int(x) for x in input().split()]
max1 = get_max(a)
a.remove(max1)
max2 = get_max(a)
print(max1 * max2)
