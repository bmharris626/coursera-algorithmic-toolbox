# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum, current, next = 0, 0, 1
    for i in range(to + 1):
        if i >= from_: sum += current
        current, next = next, current + next
    return sum % 10

def fibonacci_partial_sum(m, n):
    if n <= 1: return n
    fib = [0, 1]
    prv, cur = 0, 1
    for i in range(0, 59):
        prv, cur = cur, (prv + cur) % 10
        if i == n - 2:
            fib.append(cur % 10)
            return sum(fib[m:n+1]) % 10
        fib.append(cur)
    sm = sum(fib[m%60:]) + sum(fib[:n%60 + 1])
    return sm % 10

if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))
