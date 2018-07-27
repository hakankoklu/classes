# Uses python3


def binary_search(a, x):
    left, right = 0, len(a)
    while left < right:
        med = (left + right) // 2
        if x == a[med]:
            return med
        elif x < a[med]:
            right = med
        else:
            left = med + 1
    return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


sorted_nums = [int(x) for x in input().split()][1:]
nums_to_check = [int(x) for x in input().split()][1:]
outs = []
for x in nums_to_check:
    outs.append(binary_search(sorted_nums, x))
print(' '.join([str(x) for x in outs]))
