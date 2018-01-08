# Uses python3
import sys

def optimal_weight(W, w):
    w.insert(0, 0)
    value = dict()
    n = len(w)
    for i in range(n + 1):
        for wt in range(W + 1):
            if i == 0 or wt == 0: value[(wt, i)] = 0
            else:
                value[(wt, i)] = value[(wt, i - 1)]
                if w[i] <= wt:
                    val = value[(wt-w[i], i-1)] + w[i]
                    if val > value[(wt, i)]: value[(wt, i)] = val
    return value[(W, n)]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
