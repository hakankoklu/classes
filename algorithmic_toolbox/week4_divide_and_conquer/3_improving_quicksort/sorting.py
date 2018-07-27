# Uses python3
import random


def partition3(a, l, r):
    x = a[l]
    j = l
    m = l
    for i in range(l + 1, r + 1):
        if a[i] < x:
            j += 1
            a[i], a[j] = a[j], a[i]
        elif a[i] == x:
            j += 1
            m += 1
            if i == j or m == j:
                a[i], a[m] = a[m], a[i]
            else:
                a[i], a[m] = a[m], a[i]
                a[i], a[j] = a[j], a[i]
    for i in range(m - l + 1):
        a[l + i], a[j - i] = a[j - i], a[l + i]
    return l + j - m + 1, j


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m_start, m_end = partition3(a, l, r)
    randomized_quick_sort(a, l, m_start - 1)
    randomized_quick_sort(a, m_end + 1, r)


_ = input()
numbers = [int(x) for x in input().split()]
randomized_quick_sort(numbers, 0, len(numbers) - 1)
print(' '.join([str(x) for x in numbers]))
