for _ in ' '*int(input()):
    a, b = map(int, input().split())
    print(f'f = {a*b/(a+b):.1f}')
