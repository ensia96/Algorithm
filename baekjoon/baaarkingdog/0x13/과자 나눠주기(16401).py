M, _ = map(int, input().split())
L = [*map(int, input().split())]
s, e = 0, max(L)
while s < e:
    m = (s+e+1)//2
    if sum(l//m for l in L) >= M:
        s = m
    else:
        e = m-1
print(s)
