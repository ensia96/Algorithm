n = int(input())
d = [0, 1, 2, 3]+[0]*(n-3)
for i in range(3, n+1):
    d[i] = (d[i-1]+d[i-2]) % 15746
print(d[n])
