#Uses python3
import sys
import math

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return round(d, 4)

def closest_pair(P):
    n = len(P)
    if n == 1: return float('inf')
    if n == 2: return distance(P[0], P[1])
    mid = int(n/2)
    dl = closest_pair(P[:mid])
    dr = closest_pair(P[mid:])
    xi, yi = P[mid]
    d = min([dl, dr])
    M = list()
    for p in P:
        if xi < p[0] - d: continue
        if xi > p[0] + d: continue
        M.append(p)
    M.sort(key=lambda p: p[1])
    dm = float('inf')
    mn = len(M)
    for i, p in enumerate(M):
        if i + 1 > (mn - 1): continue
        dk = distance(p, M[i + 1])
        if dk < dm: dm = dk
    return min([dl, dr, dm])

def minimum_distance(x, y):
    P = list(zip(x, y))
    P.sort()
    return closest_pair(P)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
