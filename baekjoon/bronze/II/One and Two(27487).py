for l in [*open(i := 0)][2::2]:
    (*A,) = map(int, l.split())
    n = A.count(2)
    while A[:i].count(2) < n // 2:
        i += 1
    print([[i, -1][n % 2], 1][n < 1])
