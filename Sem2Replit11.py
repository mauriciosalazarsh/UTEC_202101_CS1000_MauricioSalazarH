num = 1023

base = 2
# Primera división
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

# Quinta división
residuo = cociente % base
cociente = cociente // base
bit5 = residuo

# Sexta división
residuo = cociente % base
cociente = cociente // base
bit6 = residuo

# Séptima división
residuo = cociente % base
cociente = cociente // base
bit7 = residuo

# Octava división
residuo = cociente % base
cociente = cociente // base
bit8 = residuo

# Novena división
residuo = cociente % base
cociente = cociente // base
bit9 = residuo

# Décima división
residuo = cociente % base
cociente = cociente // base
bit10 = residuo

print("{} = {}{}{}{}{}{}{}{}{}{}".format(num,bit10,bit9,bit8,bit7,bit6,bit5,bit4,bit3,bit2,bit1))