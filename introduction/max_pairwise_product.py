# Uses python3
def MaxPairwiseProduct(a):
    result = 0
    x, y = 0, 0
    for i in range(0, len(a) - 1):
        for j in range(i+1, len(a)):
            if a[i]*a[j] > result:
                x, y = a[i], a[j]
                result = a[i]*a[j]
    return [(x,y), result]

def MaxPairwiseProduct_fast(a):
    i, j = 0, 0
    for x in a:
        if x > i:
            j = i
            i = x
        elif x > j:
            j = x
    return [(i, j), i * j]

def stress_test(mx, nx, ax):
    i = 0
    while True:
        n = random.randint(0, nx) + 2
        print(n)
        a = [random.randint(0, ax) for i in range(n)]
        print(a)
        res1 = MaxPairwiseProduct(a)
        res2 = MaxPairwiseProduct_fast(a)
        if (res1[1] != res2[1]):
            print("Wrong answer:", res1, res2)
            break
        elif i == mx: break;
        else: print("OK")
        i += 1

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    assert(len(a) == n)
    result = MaxPairwiseProduct_fast(a)
    print(result[1])

if __name__ == '__main__':
    # stress_test(1000, 100, 10000)
    main()
