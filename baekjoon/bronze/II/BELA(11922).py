_, b, *A = open(0).read().split()
print(
    sum(
        [11, 11, 4, 4, 3, 3, 2, 20, 10, 10, 0, 14, 0, 0, 0, 0][
            2 * "AKQJT987".index(x) + (y == b)
        ]
        for x, y in A
    )
)
