P, Q = map(int, input().split())
for p in range(1, P+1):
    if P % p < 1:
        for q in range(1, Q+1):
            if Q % q < 1:
                print(p, q)
