n = int(input())
print(
    *min(
        min(
            ((i * j + n // j + n // i), i, j, n // i // j)
            for j in range(1, int((n // i) ** 0.5) + 1)
            if not ((n // i) % j)
        )
        for i in range(1, int(n**0.5) + 1)
        if not (n % i)
    )[1:]
)
