# Uses python3
def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10


def get_pisano(m):
    previous = 0
    current = 1

    n = 10000
    count = 0
    for _ in range(n - 1):
        count += 1
        previous, current = current, (previous + current) % m
        if (previous, current) == (0, 1):
            return count


def get_fibonacci_huge_fast(n, m):
    pisano_period = get_pisano(m)
    n_new = n % pisano_period

    if n_new <= 1:
        return n_new
    previous = 0
    current = 1
    for _ in range(n_new - 1):
        previous, current = current, (previous + current) % m
    return current


def calc_fib_ld_fast(n):
    if n <= 1:
        return n
    return get_fibonacci_huge_fast(n, 10)


def fibonacci_sum_squares_fast(n):
    if n <= 1:
        return n
    fibn = calc_fib_ld_fast(n)
    fibn_1 = calc_fib_ld_fast(n - 1)
    return (fibn * (fibn_1 + fibn)) % 10


n = int(input())
print(fibonacci_sum_squares_fast(n))
