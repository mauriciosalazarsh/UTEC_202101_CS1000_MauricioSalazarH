num = 48

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

print("{} = {}{}".format(num, bit2, bit1))