import math

a = int(input('a'))
b = int(input('b'))
c = int(input('c'))

x1 = (-b +  math.sqrt(b**2-4*a*2))/2*a
x2 = (-b -  math.sqrt(b**2-4*a*c))/2*a

print(x2)