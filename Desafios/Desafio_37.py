número = int(input("Digite um número inteiro: "))
binário = bin(número)
octal = oct(número)
hexa = hex(número)

print("Decimal: ", número)
print("Binário: ", binário[2:])
print("Octal: ", octal[2:])
print("Hexadecimal: ", hexa[2:])
