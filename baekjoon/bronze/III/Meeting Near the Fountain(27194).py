import math
n, t, m, x, y = map(int, open(0).read().split())
print(math.ceil(m/(60*x)+(n-m)/(60*y)-t))
