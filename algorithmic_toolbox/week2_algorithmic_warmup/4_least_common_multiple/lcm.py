# Uses python3
def gcd_fast(a, b):
    if b > a:
        a, b = b, a
    if b == 0:
        return a
    return gcd_fast(b, a % b)


def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l
    return a*b


def lcm_fast(a, b):
    d = gcd_fast(a, b)
    p = int(a/d)
    return p * b


a, b = map(int, input().split())
print(lcm_fast(a, b))
