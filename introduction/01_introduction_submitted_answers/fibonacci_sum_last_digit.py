# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1: return n
    previous, current, sum = 0, 1, 1
    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current
    return sum % 10

def fibonacci_sum(n):
    if n <= 1: return n
    fib = [0, 1]
    prv, cur, sm = 0, 1, 1
    for i in range(0, 59):
        prv, cur = cur, (prv + cur) % 10
        sm = (sm + cur) % 10
        if i == n - 2: return sm
        fib.append(sm)
    sm = ((n // 60) * sm) % 10
    return (sm + fib[n % 60]) % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum(n))
