def h(n, s, e):
    if n == 1:
        print(s, e)
        return

    h(n - 1, s, 6 - s - e)
    print(s, e)
    h(n - 1, 6 - s - e, e)


n = int(input())
print(2 ** n - 1)
h(n, 1, 3)

# 풀이 참고 : https://study-all-night.tistory.com/6
