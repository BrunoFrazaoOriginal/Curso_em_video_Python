lista = []
while True:
    numero = int(input("Digite um número: "))
    lista.append(numero)
    continuar = str(input("Deseja continuar:[S/N] ")).strip().upper()[0]
    while continuar not in "SN":
        print("Opção inválida! Escolha S para Sim ou N para Não.")
        continuar = str(input("Deseja continuar:[S/N] ")).strip().upper()[0]
    if continuar == "N":
        break
if 5 in lista:
    print("O número 5 foi digitado e está na lista.")
else:
    print("O número 5 não foi digitado e não está na lista.")
print(f"Foram digitados {len(lista)} números na lista.")
lista.sort(reverse=True)
print(lista)
print("Fim do programa.")