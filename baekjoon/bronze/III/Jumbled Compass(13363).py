a, b = map(int, open(0))
print(b-a+360*((b-a <= -180)-1*(b-a > 180)))
