#int x, n, m, r, y = 1, z, s, h = 0, p = 1;
y=1
h=0
p=1
x=float(input("Enter number:"))
n=float(input("Enter base1:"))
m=float(input("Enter base2:"))
z=x
if (n!=10):
	z = 0
	while (x != 0):
		r = x % 10
		x = x / 10
		z = z + y*r
		y = y*n
while (z != 0):
	r = z%m
	z = z / m
	h = h +(p*r)
	p = p * 10
print(h)