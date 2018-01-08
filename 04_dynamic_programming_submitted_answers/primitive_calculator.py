# Uses python3
import sys

def optimal_sequence(n):
    min_ops = {1: [1]}
    for m in range(2, n+1):
        min_ops[m] = min_ops[m-1].copy()
        min_ops[m].append(min_ops[m][-1] + 1)
        sequence = min_ops[m].copy()
        for i in range(2):
            if m >= (i+2):
                if m % (i+2) == 0:
                    sequence = min_ops[m // (i+2)].copy()
                    sequence.append(sequence[-1]*(i+2))
                if len(sequence) < len(min_ops[m]): min_ops[m] = sequence
    return min_ops[n]

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
