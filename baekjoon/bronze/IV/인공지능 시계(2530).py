a, b, c = map(int, input().split())
B, c = divmod(c+int(input()), 60)
A, b = divmod(b+B, 60)
_, a = divmod(a+A, 24)
print(a, b, c)
