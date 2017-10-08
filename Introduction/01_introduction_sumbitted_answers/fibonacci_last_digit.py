# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1: return n
    previous = 0
    current  = 1
    for _ in range(n - 1):
        previous, current = current, previous + current
    return current % 10

def fibonacci_last_digit(n):
    if n <= 1: return n
    fib = [0, 1]
    prv, cur = 0, 1
    for i in range(0, 59):
        prv, cur = cur, (prv + cur) % 10
        if i == n - 2: return cur % 10
        fib.append(cur)
    return fib[n % 60]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_last_digit(n))
