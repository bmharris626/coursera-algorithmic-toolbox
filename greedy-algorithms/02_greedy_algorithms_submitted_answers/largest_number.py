#Uses python3

import sys

def IsGreaterOrEqual(digit, maxDigit):
    if maxDigit == -float('inf'): return True
    if digit == maxDigit: return True
    digit, maxDigit = str(digit), str(maxDigit)
    n = min(len(digit), len(maxDigit))
    if (digit[:n] > maxDigit[:n]): return True
    if (digit[:n] == maxDigit[:n]) and (digit[:-n-1:-1] > maxDigit[:-n-1:-1]):
        return True
    return False

def largest_number(a):
    res = str()
    while len(a) > 0:
        maxDigit = -float('inf')
        for n in a:
            if IsGreaterOrEqual(n, maxDigit): maxDigit = n
        res += str(maxDigit)
        a.remove(maxDigit)
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
