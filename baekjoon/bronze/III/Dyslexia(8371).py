_, a, b = open(0)
print(sum(x != y for x, y in zip(a, b)))
