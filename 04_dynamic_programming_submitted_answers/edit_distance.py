# Uses python3
def edit_distance(s, t):
    s = list(s)
    t = list(t)
    s.insert(0, 0)
    t.insert(0, 0)
    n, m = len(s), len(t)
    D = [[i] for i in range(n)]
    D[0] = [j for j in range(m)]
    for j in range(1, m):
        for i in range(1, n):
            insertion = D[i][j-1] + 1
            deletion = D[i-1][j] + 1
            match = D[i-1][j-1]
            mismatch = D[i-1][j-1] + 1
            if s[i] == t[j]:
                D[i].append(min([insertion, deletion, match]))
            else:
                D[i].append(min([insertion, deletion, mismatch]))
    return D[n-1][m-1]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
