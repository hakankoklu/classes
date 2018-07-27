# Uses python3
def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

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


n = int(input())
print(fibonacci_sum_fast(n))
