# Uses python3
import sys
import random

def partition3(a, l, r):
    """
    a => list of numbers being sorted
    l => starting index of the list
    r => the last index of the list

    Checks the list from index (l + 1) to r for values that are less than or 
    equal to a[l]. If the value is equal to or less than a[1] it is moved to 
    the right of a[l] represented by the index m1. If the value is equal
    a[l] then the value is moved from poition m1 to the beginning of the
    values to the left of a[l] represented by m2. The function then returns
    the values m1, and (m1 -j) representing the two halves of the list that
    are still unsorted. (List1 = a[l:(m2-j)], List2[m1:r])
    """
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
    """
    a => list of numbers to be sorted
    l => starting index of the list
    r => the last index of the list

    First checks if the first index(l) is greater or equal to index(r), if True
    then a must have only 1 element and so the list is just returned. If False
    then the function selects a random value from the list and switches the
    value with the first element of the list. Then partion3 is called sort the
    list into values smaller than the value and larger then the value,
    represented by m1, and m2. The function then makes a recursive call to
    itself with new lists a[(m1+1):r], and a[l:m2].
    """
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
