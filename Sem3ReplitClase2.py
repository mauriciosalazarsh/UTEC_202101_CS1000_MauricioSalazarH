print("Sistema Decimal")
print("="*40)
num1 = '10'
num2 = '3'
num1 = int(num1)
num2 = int(num2)
res = num1 +num2
print(res)
print()
print("De Binario a Decimal")
print("="*40)
num='0b110'
decimal=int(num,2)
print("{} en decimal es {}".format(num, decimal))
print()
print("De Decimal a Binario")
print("="*40)
decimal = 6
enBinario = bin(decimal)
enBinario2 = enBinario[2:]
print("{} en binario es {}".format(decimal, enBinario))
print("{} en binario es {}".format(decimal, enBinario2))
print()
print("De Octal a Decimal")
print("="*40)
num = '0o10'
decimal = int(num, 8)
print("{} en decimal es {}".format(num,decimal))
print()
print("De Decimal a Octal")
print("="*40)
num = 8
enOctal = oct(num)
enOctal2 = enOctal[2:]
print("{} en octal es {}".format(num, enOctal))
print("{} en octal es {}".format(num, enOctal2))
print()
print("De Hexadecimal a Decimal")
print("="*40)
num = '0x12'
decimal = int(num, 16)
print("{} en decimal es {}".format(num, decimal))
print()
print("De Decimal a Hexadecimal")
print("="*40)
num = 18
enHexadecimal = hex(num)
enHexadecimal2 = enHexadecimal[2:]
print("{} en hexadecimal es {}".format(num, enHexadecimal))
print("{} en hexadecimal es {}".format(num, enHexadecimal2))
print()
print("Operadores Relacionales")
print("="*40)
rp = 19+20 < 89+7
print('"19+20 < 89+7" es igual a {}'.format(rp))
rp = 4|3 < 3|3
print('"4|3 < 3|3" es igual a {}'.format(rp))
rp = 7&5 == 5|0
print('"7&5 == 5|0" es igual a {}'.format(rp))