# Uses python3
import sys

def optimal_summands(n):
    summands, i = [], 1
    for i in range(1, n + 1):
        if (i == n) or (2*i + 1 <= n):
            summands.append(i)
            n -= i
        if n == 0: return summands
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
