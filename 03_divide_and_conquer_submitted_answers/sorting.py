# Uses python3
import sys
import random

def partition3(a, l, r):
    x = a[l]
    m1, m2 = l, l
    for i in range(l + 1, r + 1):
        y = a[i]
        if y <= x:
            m1 += 1
            a[i], a[m1] = a[m1], a[i]
        if y == x:
            m2 += 1
            a[m1], a[m2] = a[m2], a[m1]
    j = 0
    for i in range(l, m2 + 1):
        a[i], a[m1 - j] = a[m1 - j], a[i]
        j += 1
    return m1, m1 - j

def randomized_quick_sort(a, l, r):
    if l >= r: return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m2)
    randomized_quick_sort(a, m1 + 1, r)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
