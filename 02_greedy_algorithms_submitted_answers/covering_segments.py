# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    segments.sort(key=lambda s: s.end)
    points, n, N = [], 0, len(segments)
    start = segments[n].start
    while n < N:
        end = segments[n].end
        points.append(end)
        while (n < N) and (start <= end):
            start = segments[n].start
            if start <= end: n += 1
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
