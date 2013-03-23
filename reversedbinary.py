x = input()
x = "{0:b}".format(x)
x = list(x)
for y in range(len(x)/2):
	z = x[y]
	x[y] = x[len(x)-1-y]
	x[len(x)-1-y] = z
print int("".join(x), 2)