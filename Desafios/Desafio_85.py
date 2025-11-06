valores = [[], []]
for n in range(0, 7):
    numero = int(input(f"Digite o {n+1}º valor: "))
    if numero != 0:
        if numero % 2 == 0:
            valores[0].append(numero)
        else:
            valores[1].append(numero)
valores[0].sort()
valores[1].sort()
print("-=" * 30)
print(f"Os números pares, são: {valores[0]}")
print(f"Os números ímpares, são: {valores[1]}")
print("-=" * 30)