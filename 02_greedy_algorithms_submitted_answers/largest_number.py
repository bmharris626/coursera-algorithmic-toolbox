#Uses python3

import sys

def IsGreaterOrEqual(digit, maxDigit):
    if maxDigit == -float('inf'): return True
    t1 = int(str(digit) + str(maxDigit))
    t2 = int(str(maxDigit) + str(digit))
    return t1 >= t2

def largest_number(Digits):
    answer = str()
    while len(Digits) > 0:
        maxDigit = -float('inf')
        for digit in Digits:
            if IsGreaterOrEqual(digit, maxDigit): maxDigit = digit
        answer += str(maxDigit)
        Digits.remove(maxDigit)
    return answer

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
