print(max([d, 10+[c, b][c < d], 5*[20+b*2, 4+a+c][b < c], 500+a*50]
      [-len({a, b, c, d})]for i in [*open(0)][1:]for a, b, c, d in sorted(map(int, i.split())))*100)
