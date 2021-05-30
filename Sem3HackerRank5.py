import math

a = int(input())
b = int(input())

x = not(math.sqrt(a**2 + b**2) == (2*a - b))
x = x*1
print(x)