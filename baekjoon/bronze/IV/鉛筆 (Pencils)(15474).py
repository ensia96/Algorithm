n, a, b, c, d = map(int, input().split())
x, y = divmod(n, a)
X = x+bool(y)
x, y = divmod(n, c)
Y = x+bool(y)
print(min(X*b, Y*d))
