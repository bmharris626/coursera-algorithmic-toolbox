# python3

def naive_gcd(a, b):
    best = 0
    for d in range(1, a + b + 1):
        if (a % d == 0) and (b % d == 0):
            best = d
    return best

def euclid_gcd(a, b):
    if b == 0: return a
    return euclid_gcd(b, a % b)

def main():
    a = [int(x) for x in input().split()]
    assert len(a) == 2
    print(euclid_gcd(a[0], a[1]))

if __name__ == '__main__':
    main()
