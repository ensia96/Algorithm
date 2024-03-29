import sys
sys.setrecursionlimit(10**9)
I = sys.stdin.readline
n = int(I())+1
C, D, V = [[]for _ in ' '*n], [[0, 1] for _ in ' '*n], [0]*n
for _ in ' '*(n-2):
    u, v = map(int, I().split())
    C[u] += [v]
    C[v] += [u]


def F(c):
    V[c] = 1
    for n in C[c]:
        if not V[n]:
            F(n)
            D[c][0] += D[n][1]
            D[c][1] += min(D[n])


F(1)
print(min(D[1]))
