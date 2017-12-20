# Uses python3
import sys

def fast_count_segments(starts, ends, points):
    S = list(zip(starts, 's'*len(starts)))
    E = list(zip(ends, 'e'*len(ends)))
    P = list(zip(points, 'p'*len(points)))
    A = S + E + P
    A.sort(key=lambda x: x[0])
    cnt = list()
    s = 0
    for a in A:
        if a[1] == 's': s += 1
        if a[1] == 'e': s -= 1
        if a[1] == 'p': cnt.append(s)
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
