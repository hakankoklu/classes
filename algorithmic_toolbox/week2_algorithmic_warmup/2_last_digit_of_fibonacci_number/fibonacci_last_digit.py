# Uses python3

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


def calc_fib_ld_fast(n):
    if (n <= 1):
        return n
    fibs = [0, 1] + [None] * (n-1)
    for i in range(2, n + 1):
        fibs[i] = (fibs[i-1] + fibs[i-2]) % 10
    return fibs[n]


n = int(input())
print(calc_fib_ld_fast(n))
