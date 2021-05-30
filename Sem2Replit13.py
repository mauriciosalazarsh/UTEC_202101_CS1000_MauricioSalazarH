base = 8
num = 3054

# Primer división
residuo = num % base
cociente = num // base
bit1 = residuo

# Segunda división
residuo = cociente % base
cociente = cociente // base
bit2 = residuo

# Tercera división
residuo = cociente % base
cociente = cociente // base
bit3 = residuo

# Cuarta división
residuo = cociente % base
cociente = cociente // base
bit4 = residuo

print("{} = {}{}{}{}".format(num, bit4, bit3, bit2, bit1))