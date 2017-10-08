# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1: return n
    previous = 0
    current  = 1
    for _ in range(n - 1):
        previous, current = current, previous + current
    return current % m

def fibonacci_huge(n, m):
    if n <= 1: return n
    fib = [0, 1]
    prv, cur = 0, 1
    for i in range(n - 1):
        prv, cur = cur, (prv + cur) % m
        fib.append(cur)
        if (fib[-2] == 0) and (fib[-1] == 1):
            return fib[n % (len(fib) - 2)]
    return cur

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(fibonacci_huge(n, m))
