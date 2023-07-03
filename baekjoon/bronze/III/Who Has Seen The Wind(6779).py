h, m = map(int, open(0))
for t in range(1, m+1):
    x = -6*t**4+h*t**3+2*t*t+t
    if x <= 0:
        break
print('The balloon', *[['first touches ground at hour:', t],
      ['does not touch ground in the given time.']][t == m])
