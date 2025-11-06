soma = maior = menor = contador = 0

continuar = "S"
while continuar == "S":
    n = int(input("Digite um número inteiro: "))
    soma += n
    contador += 1

    if maior == 0 or n > maior:
        maior = n
    if menor == 0 or n < menor:
        menor = n

    continuar = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
    while continuar not in ("S", "N"):
        print("Opção inválida! Tente novamente.")
        continuar = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]

    media = soma / contador
print("Você digitou {} números.".format(contador))
print("A média dos números digitados é {}.".format(media))
print("O maior número digitado é {}.".format(maior))
print("O menor número digitado é {}.".format(menor))
