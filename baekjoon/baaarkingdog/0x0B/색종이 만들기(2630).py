n = int(input())
A = [0]*2


def S(n, P):
    if n == 1:
        A[P[0]] += 1
        return
    for i in range(2):
        T = P[i*(n//2):(i+1)*(n//2)]
        for j in range(2):
            t = [t[j*(n//2):(j+1)*(n//2)]for t in T]
            if sum(map(sum, t)) in [0, (n//2)**2]:
                A[t[0][0]] += 1
                continue
            S(n//2, t)


S(n, [[*map(int, input().split())]for _ in ' '*n])
print(*A, sep='\n')
