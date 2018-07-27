# Uses python3
def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10


def fibonacci_sum_fast(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sums = [0, 1] + [None] * 58

    for i in range(2, 60):
        previous, current = current, (previous + current) % 10
        sums[i] = (sums[i - 1] + current) % 10

    return sums[n % 60]


def fibonacci_partial_sum_fast(m, n):
    total = fibonacci_sum_fast(n)
    excess = fibonacci_sum_fast(m - 1) if m > 0 else 0

    return (total - excess) % 10


m, n = [int(x) for x in input().split()]
print(fibonacci_partial_sum_fast(m, n))
