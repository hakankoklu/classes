# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


def calc_fib_fast(n):
    if (n <= 1):
        return n
    fibs = [0, 1] + [None] * (n-1)
    for i in range(2, n + 1):
        fibs[i] = fibs[i-1] + fibs[i-2]
    return fibs[n]


n = int(input())
print(calc_fib_fast(n))
