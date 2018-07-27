def FastModularExponentiation(b, e, m):
    """ computes b ** e (mod m) """
    if e == 0:
        return 1
    bin_e = [int(x) for x in list(bin(e)[2:])]
    bin_e.reverse()
    print(bin_e)
    exps = []
    c = b % m
    e_temp = 1
    while e_temp <= e:
        exps.append(c)
        c = c ** 2
        c = c % m
        e_temp = 2 * e_temp
    print(exps)
    result = 1
    for x, y in zip(exps, bin_e):
        if y == 1:
            result = (result * x) % m
    return result


b, e, m = [int(x) for x in input().split()]
print(FastModularExponentiation(b, e, m))
