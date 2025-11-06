from time import sleep
n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))
operação = 0
while operação != "5":
    print("=" * 20)
    print("""
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    """)
    print("=" * 20)
    operação = str(input(">>>>>>>> Escolha uma opção: "))
    if operação == "1":
        operação = n1 + n2
        print("Você escolheu somar, então {} + {} = {}.".format(n1, n2, operação))
    elif operação == "2":
        operação = n1 * n2
        print("Você escolher multiplicar, então {} * {} = {}.".format(n1, n2, operação))
    elif operação == "3":
        if n1 > n2:
            print("Você escolheu maior, e {} é maior que {}.".format(n1, n2))
        if n1 < n2:
            print("Você escolheu maior, e {} é maior que {}.".format(n2, n1))
        else:
            print("Você escolheu maior, mas {} é igual a {}.".format(n1, n2))
    elif operação == "4":
        n1 = float(input("Digite um número novo: "))
        n2 = float(input("Digite outro número novo: "))
        print("Você escolheu novos números, e digitou {} e {}.".format(n1, n2))
    elif operação == "5":
        print("Você escolheu sair.")
        sleep(0.5)
        print("Saindo do programa.")
        sleep(0.5)
    else:
        print("Opção inválida! Tente novamente.")
    sleep(2)
sleep(1)
print("Fim")
