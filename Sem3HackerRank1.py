a = int(input())
b = int(input())

x = ((a != b) or (a >= b)) and (a%b == 1)
x = x*1
print(x)