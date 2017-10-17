import cmath
import math

ch = True

while ch:
	try:
		a = float(input('> a: '))
		b = float(input('> b: '))
		c = float(input('> c: '))
		ch = False

	except:
		print('erro: digite um número!')

delta = b**2 - 4 * a * c

if delta < 0:
	x1 = (-b + cmath.sqrt(delta))/2*a
	x2 = (-b - cmath.sqrt(delta))/2*a

else:
	x1 = (-b + math.sqrt(delta))/2*a
	x2 = (-b - math.sqrt(delta))/2*a

print(x1,x2)