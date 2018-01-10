# Uses python3
import sys

def optimal_weight(W, w):
    w.insert(0, 0)
    value = [list() for i in range(W + 1)]
    i = 0
    for wt in range(W + 1):
        for i, wi in enumerate(w):
            if i == 0 or wt == 0: value[wt].append(0)
            else:
                value[wt].append(value[wt][i-1])
                if wi <= wt:
                    val = value[wt-wi][i-1] + wi
                    if val > value[wt][i]: value[wt][i] = val
    return value[W][i]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
