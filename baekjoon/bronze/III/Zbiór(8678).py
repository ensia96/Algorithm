for l in [*open(0)][1:]:
    a, b = map(int, l.split())
    print('tnaike'[b % a > 0::2])
