def PowMod(a, n, mod):
    if n == 0:
        return 1 % mod
    elif n == 1:
        return a % mod
    else:
        b = PowMod(a, n // 2, mod)
        b = b * b % mod
        if n % 2 == 0:
          return b
        else:
          return b * a % mod


def ExtendedEuclid(a, b):
    if b == 0:
        return (1, 0)
    (x, y) = ExtendedEuclid(b, a % b)
    k = a // b
    return (y, x - k * y)


def InvertModulo(a, n):
    (b, x) = ExtendedEuclid(a, n)
    if b < 0:
        b = (b % n + n) % n
    return b


# You also have access to the function ConvertToInt(message)ConvertToInt(message) which converts a text message to an integer.

def ConvertToInt(message_str):
    res = 0
    for i in range(len(message_str)):
        res = res * 256 + ord(message_str[i])
    return res


def ConvertToStr(n):
    res = ""
    while n > 0:
        res += chr(n % 256)
        n //= 256
    return res[::-1]


def Encrypt(message, modulo, exponent):
    return PowMod(ConvertToInt(message), exponent, modulo)


# You have access to the function ConvertToStr(m)ConvertToStr(m) which converts from integer mm to the plaintext messagemessage.
# You also have access to the function InvertModulo(a, n)InvertModulo(a,n) which takes coprime integers aa and nn as inputs and returns integer bb such that ab \equiv 1 \bmod{n}ab≡1modn.
def Decrypt(ciphertext, p, q, exponent):
    d = InvertModulo(exponent, (p - 1) * (q - 1))
    return ConvertToStr(PowMod(ciphertext, d, p * q))


def DecipherSimple(ciphertext, modulo, exponent, potential_messages):
    # Fix this implementation
    for message in potential_messages:
        if ciphertext == Encrypt(message, modulo, exponent):
            return message
    return "don't know"


def DecipherSmallPrime(ciphertext, modulo, exponent):
    for candy in range(2, 1000000):
        if modulo % candy == 0:
            small_prime = candy
            big_prime = modulo // candy
            return Decrypt(ciphertext, small_prime, big_prime, exponent)
    return "don't know"


def IntSqrt(n):
    low = 1
    high = n
    iterations = 0
    while low < high and iterations < 5000:
        iterations += 1
        mid = (low + high + 1) // 2
        if mid * mid <= n:
            low = mid
        else:
            high = mid - 1
    return low


def DecipherSmallDiff(ciphertext, modulo, exponent):
    sq_n = IntSqrt(modulo)
    for candy in range(sq_n - 5000, sq_n + 1):
        if modulo % candy == 0:
            small_prime = candy
            big_prime = modulo // candy
            return Decrypt(ciphertext, small_prime, big_prime, exponent)
    return "don't know"


def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a % b)


def DecipherCommonDivisor(first_ciphertext, first_modulo, first_exponent, second_ciphertext, second_modulo,
                          second_exponent):
    common_prime = GCD(first_modulo, second_modulo)
    if common_prime > 1:
        q1 = first_modulo // common_prime
        q2 = second_modulo // common_prime
        return (Decrypt(first_ciphertext, common_prime, q1, first_exponent),
                Decrypt(second_ciphertext, common_prime, q2, second_exponent))
    return "unknown message 1", "unknown message 2"


def ChineseRemainderTheorem(n1, r1, n2, r2):
    (x, y) = ExtendedEuclid(n1, n2)
    return ((r2 * x * n1 + r1 * y * n2) % (n1 * n2) + (n1 * n2)) % (n1 * n2)


def DecipherHastad(first_ciphertext, first_modulo, second_ciphertext, second_modulo):
    r = ChineseRemainderTheorem(first_modulo, first_ciphertext, second_modulo, second_ciphertext)
    return ConvertToStr(IntSqrt(r))
