# Uses python3
import itertools


def partition3_new(s):
    if sum(s) % 3 != 0:
        return 0
    elif len(s) < 3:
        return 0
    target = sum(s) // 3




def partition3(A):
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0


_ = int(input())
values = [int(x) for x in input().split()]
print(partition3_new(values))

