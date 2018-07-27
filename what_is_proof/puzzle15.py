def is_permutation(p):
    return set(p) == set(range(len(p)))


def is_even_permutation(p):
    if not is_permutation(p):
        raise ValueError("Not a valid permutation!")
    sign = 0
    for ind, num in enumerate(p):
        if num != ind:
            to_switch = p.index(ind)
            p[to_switch], p[ind] = p[ind], p[to_switch]
            sign = 1 - sign
            print(p, sign)
    return sign == 0

