m, n = map(int, input().split())

n += 1
prime = [True] * n

for i in range(2, int(n ** 0.5) + 1):
    if prime[i]:
        for j in range(2 * i, n, i):
            prime[j] = False

for i in range(m, n):
    if i > 1 and prime[i]:
        print(i)

# 에라토스테네스의 체 풀이 관련 글 : https://leejunggae.tistory.com/3
