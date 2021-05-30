num = 15850
base = 16

# Primera división
residuo = num % base
cociente = num // base
bit1 = str(residuo)

bit1 = bit1.replace("10","a")
bit1 = bit1.replace("11","b")
bit1 = bit1.replace("12","c")
bit1 = bit1.replace("13","d")
bit1 = bit1.replace("14","e")
bit1 = bit1.replace("15","f")


# Segunda división
residuo = cociente % base
cociente = cociente // base
bit2 = str(residuo)

bit2 = bit2.replace("10","a")
bit2 = bit2.replace("11","b")
bit2 = bit2.replace("12","c")
bit2 = bit2.replace("13","d")
bit2 = bit2.replace("14","e")
bit2 = bit2.replace("15","f")


# Tercera división
residuo = cociente % base
cociente = cociente // base
bit3 = str(residuo)

bit3 = bit3.replace("10","a")
bit3 = bit3.replace("11","b")
bit3 = bit3.replace("12","c")
bit3 = bit3.replace("13","d")
bit3 = bit3.replace("14","e")
bit3 = bit3.replace("15","f")


# Cuarta división
residuo = cociente % base
cociente = cociente // base
bit4 = str(residuo)

bit4 = bit4.replace("10","a")
bit4 = bit4.replace("11","b")
bit4 = bit4.replace("12","c")
bit4 = bit4.replace("13","d")
bit4 = bit4.replace("14","e")
bit4 = bit4.replace("15","f")


print("{} = {}{}{}{}".format(num,bit4,bit3,bit2,bit1))