# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):
    # Split String
    D, OP = list(), list()
    for i, c in enumerate(dataset):
        if i%2 == 0: D.append(int(c))
        else: OP.append(c)
    n = len(D)
    # Allocate Max(M) and Min(m) arrays
    row = [None for i in range(n)]
    m = [row.copy() for i in range(n)]
    M = [row.copy() for i in range(n)]
    for i in range(n):
        M[i][i] = D[i]
        m[i][i] = D[i]
    # Find min and max for each cell in m, M
    for s in range(1, n):
        for i in range(n-s):
            j = i + s
            mn = float('inf')
            mx = -float('inf')
            for k in range(i, j):
                a = evalt(M[i][k], M[k+1][j], OP[k])
                b = evalt(m[i][k], M[k+1][j], OP[k])
                c = evalt(M[i][k], m[k+1][j], OP[k])
                d = evalt(m[i][k], m[k+1][j], OP[k])
                mn = min(mn, a, b, c, d)
                mx = max(mx, a, b, c, d)
            m[i][j] = mn 
            M[i][j] = mx
    return M[0][n-1]

if __name__ == "__main__":
    print(get_maximum_value(input()))
