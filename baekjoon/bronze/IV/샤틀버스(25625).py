x, y = map(int, input().split())
print(-~-(y//x % 2)*x+y % x)
