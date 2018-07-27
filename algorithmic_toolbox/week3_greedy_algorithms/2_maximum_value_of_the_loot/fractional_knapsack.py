# Uses python3


def get_optimal_value(capacity, weights, values):
    unit_values = [(value/weight, weight, value) for value, weight in zip(values, weights)]
    unit_values.sort(reverse=True)
    value = 0
    while capacity > 0:
        if not unit_values:
            break
        if unit_values[0][1] <= capacity:
            value += unit_values[0][2]
            capacity -= unit_values[0][1]
            unit_values.pop(0)
        else:
            value += unit_values[0][0] * capacity
            capacity = 0
    return value


n, capacity = [int(x) for x in input().split()]
values, weights = [], []
for i in range(n):
    value, weight = [int(x) for x in input().split()]
    values.append(value)
    weights.append(weight)
opt_value = get_optimal_value(capacity, weights, values)
print("{:.10f}".format(opt_value))
