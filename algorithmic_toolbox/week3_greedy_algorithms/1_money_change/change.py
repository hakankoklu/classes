# Uses python3


def get_change(m):
    tens = m // 10
    m = m - 10 * tens
    fives = m // 5
    m = m - 5 * fives
    return tens + fives + m


m = int(input())
print(get_change(m))
