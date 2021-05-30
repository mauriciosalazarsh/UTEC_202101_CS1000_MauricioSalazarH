num = 13

base = 8
# Primera division
residuo = num % base
cociente = num // base
bit1 = residuo

# Segunda division
residuo = cociente % base
cociente = cociente // base
bit2 = residuo

print("{} = {}{}".format(num, bit2, bit1))