for l in [*open(0)][1:]:
    print(+(4 < len(l) and "!!??!??\n" == l.replace(l[0], "!").replace(l[2], "?")))
