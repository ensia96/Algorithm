A = ['No', 'Yes']
for l in [*open(0)][1:]:
    x, y = map(int, l.split())
    print(A[x < 24 and y < 60], A[0 < x < 13 and 0 <
          y < 32-(x in [2, 4, 6, 9, 11])-(x == 2)])
