for i, l in enumerate(open(0)):
    a, *A = map(int, l.split())
    x = not a % 2
    a and print('Case', i, (A[a//2]+x*A[a//2-1])/(1+x))
