n, m = map(int, input().split())
M = 10000000
D = [n*[0]for _ in ' '*n]
A = [*map(int, input().split())]if m else[]


def f(i, a):
    if i >= n:
        return 0
    elif i+1 in A:
        D[i][a] = f(i+1, a)
    elif not D[i][a]:
        D[i][a] = min(f(i+5, a+2)+37000, f(i+3, a+1)+25000,
                      f(i+1, a)+10000, f(i+1, a-3)if a > 2 else M)
    return D[i][a]


print(f(0, 0))
