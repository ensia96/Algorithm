# from itertools import combinations as c
# n = int(input())
# s = [[*map(int, input().split())] for _ in range(n)]
# b, r = map(set, c(range(n), n//2)), {*range(n)}

# print(min(abs(sum(s[i][j] for i in c for j in c) -
# abs(sum(s[i][j] for i in r-c for j in r-c))) for c in b))

########################################################################

n = int(input())
s = [[*map(int, input().split())] for _ in range(n)]
g = {*range(n)}
l, v = lambda x: sum(s[i][j] for i in x for j in x), [1]*n


def f(a, c):
    if c == n:
        return abs(l(g-a)-l(a))
    r = 10**8
    for i in range(n):
        if v[i]:
            v[i] = 0
            r = min(r, f(a.union({i}), c+2))
            v[i] = 1
    return r


print(f(set(), 0))
