# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

i, j = 0, 0
for x in a:
    if x > i:
        j = i
        i = x

print(i * j)
