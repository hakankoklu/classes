# Uses python3


def get_majority_element(a):
    counts = count_nums(a)
    for key, value in counts.items():
        if value > len(a) // 2:
            return 1
    return 0


def count_nums(a):
    if len(a) == 1:
        return {a[0]: 1}
    m = len(a) // 2
    left = count_nums(a[:m])
    right = count_nums(a[m:])
    for key, value in right.items():
        if key in left:
            left[key] += value
        else:
            left[key] = value
    return left


_ = input()
numbers = [int(x) for x in input().split()]
print(get_majority_element(numbers))
