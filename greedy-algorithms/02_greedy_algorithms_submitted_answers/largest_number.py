#Uses python3

import sys

def IsGreaterOrEqual(digit, maxDigit):
    if maxDigit == -float('inf'): return True
    if digit == maxDigit: return True
    for x, y in zip(str(digit), str(maxDigit)):
        if x > y: return True
        elif x < y: return False
    if len(str(digit)) < len(str(maxDigit)):
        return str(digit)[-1] >= str(maxDigit)[-1]
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
