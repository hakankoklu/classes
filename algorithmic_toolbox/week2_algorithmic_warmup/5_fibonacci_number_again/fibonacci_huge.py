# Uses python3

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


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


n, m = map(int, input().split())
print(get_fibonacci_huge_fast(n, m))
