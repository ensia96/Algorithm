import sys
d, l, a = lambda: map(int, sys.stdin.readline().split()), [0], 0
n, m, *_ = [*d()] + [exec('a += i;l += [a]') for i in d()]
for _ in range(m):
    i, j = d()
    print(l[j]-l[i-1])
