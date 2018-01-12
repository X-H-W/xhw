m = [x for x in range(1,101) for j in range(2,x) if x%j == 0]
o = set(m)
print(o)
