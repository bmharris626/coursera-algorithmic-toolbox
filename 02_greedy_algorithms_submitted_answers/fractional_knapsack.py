# Uses python3
import sys

def select_optimal_ratio(weights, values):
    mx, n = 0, 0
    for i, r in enumerate(zip(weights, values)):
        ratio = 0
        if r[0] > 0: ratio = r[1] / r[0]
        if ratio > mx: n, mx = i, ratio
    return n

def get_optimal_value(capacity, weights, values):
    n, value = len(weights), 0
    A = [0 for i in range(len(weights))]
    for n in range(len(weights)):
        if capacity == 0: return value
        i = select_optimal_ratio(weights, values)
        a = min(weights[i], capacity)
        value += a * values[i] / weights[i]
        weights[i] -= a
        A[i] += a
        capacity -= a
    return value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
