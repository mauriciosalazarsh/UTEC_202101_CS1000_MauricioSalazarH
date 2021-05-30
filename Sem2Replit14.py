base = 2
num = 5785

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

# Undécima división
residuo = cociente % base
cociente = cociente // base
bit11 = residuo

# Duodécima división
residuo = cociente % base
cociente = cociente // base
bit12 = residuo

# Decimotercera división
residuo = cociente % base
cociente = cociente // base
bit13 = residuo

print("{} = {}{}{}{}{}{}{}{}{}{}{}{}{}".format(num, bit13, bit12, bit11, bit10, bit9, bit8, bit7, bit6, bit5, bit4, bit3, bit2, bit1))