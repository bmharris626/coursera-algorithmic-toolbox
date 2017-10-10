# Uses python3
import sys

def get_change(m):
    c10, m = m // 10, m % 10
    c5, m = m // 5, m % 5
    return c10 + c5 + m

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
