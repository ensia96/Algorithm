n = int(input())
d = [0, 1, 1]+[0]*(n-2)
for i in range(2, n+1):
    d[i] = d[i-1]+d[i-2]
print(d[n])
