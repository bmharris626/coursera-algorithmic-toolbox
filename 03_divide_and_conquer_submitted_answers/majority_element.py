# Uses python3
import sys

def find_candidate(A):
    candidate, count = A[0], 1
    for element in A:
        if candidate == element: count += 1
        else: count -= 1
        if count == 0:
            candidate = element
            count = 1
    return candidate

def get_majority_element(A, left, right):
    candidate = find_candidate(A)
    count = 0
    for element in A:
        if element == candidate: count += 1
    if count > (right - left) / 2: return candidate
    return -1

def majority_element_naive(A):
    for currentElement in A:
        count = 0
        for element in A:
            if currentElement == element: count += 1
        if count > len(A) / 2: return currentElement
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
