import sys
I = sys.stdin.readline
M = 2**27
n = int(I())+1
N = range(1, n)
C = [[M]*n for _ in ' '*n]
R = [[0]*n for _ in ' '*n]
for _ in ' '*int(I()):
    a, b, c = map(int, I().split())
    t = C[a][b]
    if t > c:
        C[a][b], R[a][b] = c, b
for k in N:
    C[k][k] = 0
    for i in N:
        for j in N:
            t = C[i][k]+C[k][j]
            if C[i][j] > t:
                C[i][j], R[i][j] = t, R[i][k]
for l in C[1:]:
    print(*(0 if i == M else i for i in l[1:]))
for i in N:
    for j in N:
        if C[i][j] in [0, M]:
            print(0)
            continue
        r = [i]
        while r[-1] != j:
            r += R[r[-1]][j],
        print(len(r), *r)
