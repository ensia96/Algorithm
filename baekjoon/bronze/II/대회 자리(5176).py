i = input
exec('p=int(i().split()[0]);print(p-len({*map(i," "*p)}));'*int(i()))
