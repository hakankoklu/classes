# Uses python3


def optimal_sequence(target):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)


def calc_dp(target):
    previous_stop = [0] * (target + 1)
    stop_count = [0, 0] + [float('inf')] * (target - 1)
    for i in range(2, target + 1):
        if i % 3 == 0 and stop_count[i] > stop_count[i // 3] + 1:
            stop_count[i] = stop_count[i // 3] + 1
            previous_stop[i] = i // 3
        if i % 2 == 0 and stop_count[i] > stop_count[i // 2] + 1:
            stop_count[i] = stop_count[i // 2] + 1
            previous_stop[i] = i // 2
        if stop_count[i] > stop_count[i - 1] + 1:
            stop_count[i] = stop_count[i - 1] + 1
            previous_stop[i] = i - 1
    result = [target]
    current = target
    while current != 1:
        result.append(previous_stop[current])
        current = previous_stop[current]
    result.reverse()
    return stop_count[target], result


n = int(input())
steps, sequence = calc_dp(n)
print(steps)
print(' '.join([str(x) for x in sequence]))
