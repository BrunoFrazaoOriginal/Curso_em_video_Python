pessoas = int(input("Quantas pessoas vão se pesar? "))

maior = 0
menor = 0

for n in range(pessoas):
    peso = float(input("Digite o peso da {}ª pessoa (kg): ".format(n+1)))
    if n == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print("A pessoa mais pesada, tem {}kg.".format(maior))
print("A pessoa mais leve, tem {}kg.".format(menor))
