a = int(input())
b = int(input())

bin_a = bin(a)
bin_b = bin(b)

a = (bin_a[3:6])
b = (bin_b[3:6])

x = a == b
x = x*1
print(x)
