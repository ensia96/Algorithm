n, a, b = map(int, open(0).read().split())
print('Deletion', ['failed', 'succeeded'][[a == b, not (a & b)][n % 2]])
