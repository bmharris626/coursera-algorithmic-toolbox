# Uses python3
import sys, random

def lte(a, b):
    d = {'p': 1, 's': 0, 'e': 2}
    if a == b: return True
    if a[0] == b[0]: return d[a[1]] < d[b[1]]
    return a[0] < b[0]

def binary_search(A, key):
    low, high = 0, len(A) - 1
    while low <= high:
        mid = int(low + (high - low) / 2)
        if key == A[mid]: return mid
        elif key < A[mid]: high = mid - 1
        else: low = mid + 1
    return -1

def partition3(a, l, r):
    x = a[l]
    m1, m2 = l, l
    for i in range(l + 1, r + 1):
        y = a[i]
        if lte(y, x):
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

def fast_count_segments(starts, ends, points):
    a = list(zip(starts, len(starts)*'s'))
    a.extend(list(zip(ends, len(ends)*'e')))
    a.extend(list(zip(points, len(points)*'p')))
    randomized_quick_sort(a, 0, len(a) - 1)
    n = len(ends)
    s, e, = 0, n
    p = dict()
    for element, typ in a:
        if typ == 'e': e -= 1
        elif typ == 's': s += 1
        else: p[element] = e + s - n
    cnt = list()
    for pnt in points:
        cnt.append(p[pnt])
    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
