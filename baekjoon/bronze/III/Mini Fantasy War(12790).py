for _ in ' '*int(input()):
    a, b, c, d, e, f, g, h = map(int, input().split())
    print(max(1, a+e)+5*max(1, b+f)+2*(max(0, c+g)+d+h))
