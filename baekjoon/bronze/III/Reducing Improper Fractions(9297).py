for i in range(int(input())):
    a, b = map(int, input().split())
    x, y = divmod(a, b)
    print(
        f"Case {i+1}:{' '+str(x)if x else''}{f' {y}/{b}'if y else''}{' 0' if a==0 else''}")
