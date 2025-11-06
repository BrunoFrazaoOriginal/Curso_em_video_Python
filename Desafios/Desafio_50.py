soma = 0
for n in range(0, 6):
    pares = int(input("Digite um número: "))
    if pares % 2 == 0:
        soma += pares
print("A soma dos valores pares é de {}.".format(soma))
