# python3

def euclid_gcd(a, b):
    if b == 0: return a
    return euclid_gcd(b, a % b)

def lcm(a, b):
    gcd = euclid_gcd(a, b)
    return (a * b) // gcd

def main():
    a = [int(x) for x in input().split()]
    assert len(a) == 2
    print(lcm(a[0], a[1]))

if __name__ == '__main__':
    main()
