for l in [*open(0)][1:]:
    y, m, d = map(int, l.split())
    print(196471 - (~-y * 195 + ~-y // 3 * 5 - (y % 3 > 0) * ~-m // 2 + ~-m * 20 + d))
