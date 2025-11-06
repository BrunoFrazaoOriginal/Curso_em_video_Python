valores = []
while True:
    numero = int(input("Digite um valor inteiro: "))
    if numero not in valores:
        print("Valor adicionado com sucesso.")
    while numero in valores:
        print("Valor já adicionado! Esse valor não será computado.")
        numero = int(input("Digite um valor inteiro: "))
    valores.append(numero)
    continuar = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    while continuar not in "SN":
        print("Opção inválida! Escolha S para continuar ou N para parar.")
        continuar = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if continuar == "N":
            break
print("-=" * 30)
print("Os valores adicionados, são: ", end=" ")
valores.sort()
print(valores)