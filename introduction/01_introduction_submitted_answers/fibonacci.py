#python3

def fibonacci(n):
    if n <= 1: return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_fast(n):
    if n <= 1: return n
    fib = list()
    for i in range(0, n):
        if i <= 1: fib.append(i)
        else: fib.append(fib[i-1] + fib[i-2])
    return fib[n-1] + fib[n-2]

def main():
    n = int(input())
    print(fibonacci_fast(n))

if __name__ == '__main__':
    main()
