# Uses python3
import sys

def merge_sort(A):
    n = len(A)
    num_of_inversions = 0
    if n == 1: return A, num_of_inversions
    m = n // 2
    B, b = merge_sort(A[:m])
    C, c = merge_sort(A[m:])
    A1, a = merge(B, C)
    num_of_inversions += c + b + a
    return A1, num_of_inversions

def merge(B, C):
    D = list()
    num_of_inversions = 0
    while (len(B) > 0) and (len(C) > 0):
        if B[0] <= C[0]:
            D.append(B.pop(0))
        else:
            D.append(C.pop(0))
            num_of_inversions += len(B)
    D.extend(B)
    D.extend(C)
    return D, num_of_inversions

def get_number_of_inversions(a, b, left, right):
    A, number_of_inversions = merge_sort(a)
    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
