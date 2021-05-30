a = float(input())
b = float(input())

astr = str(a)[:5]
afloat = float(astr)

x = afloat == b
x = x*1
print(x)