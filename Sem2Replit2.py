num = 18

base = 8
# Primera división
residuo = num % base
cociente = num // base
bit1 = residuo

# Segunda división
residuo = cociente % base
cociente = cociente // base
bit2 = residuo

print("{} = {}{}".format(num, bit2, bit1))
