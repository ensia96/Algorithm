n = int(input())
s = [[*map(int, input().split())] for _ in range(n)]
g = {*range(n)}
l, v = lambda x: sum(s[i][j] for i in x for j in x), [1]*n


def f(a, i, c):
    if c == n:
        return abs(l(g-set(a))-l(a))
    r = 10**8
    for d in range(i, n):
        if v[d]:
            v[d] = 0
            r = min(r, f(a+[d], d, c+2))
            v[d] = 1
    return r


print(f([], 0, 0))
