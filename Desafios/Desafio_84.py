lista_total = []
dados = []
qtd = pesado = leve = 0

while True:
    dados.append(str(input("Digite nome da pessoa: ")))
    dados.append(float(input("Digite o peso da pessoa: ")))
    lista_total.append(dados[:])
    dados.clear()
    qtd += 1

    if qtd == 1:
        pesado = leve = lista_total[0][1]
    else:
        if lista_total[-1][1] > pesado:
            pesado = lista_total[-1][1]
        if lista_total[-1][1] < leve:
            leve = lista_total[-1][1]

    continuar = str(input("Deseja cadastrar mais uma pessoa? [S/N] ")).strip().upper()[0]
    while continuar not in "SN":
        print("Opção inválida! Digite S para continuar ou N para encerrar.")
        continuar = str(input("Deseja cadastrar mais uma pessoa? [S/N] ")).strip().upper()[0]
    if continuar == "N":
        break

print(f"{qtd} pessoas foram cadastradas")
print(f"O maior peso encontrado, foi {pesado:.2f}kg. Pessoa mais pesada:")
for pessoa in lista_total:
    if pessoa[1] == pesado:
        print(f" - [{pessoa[0]}]")
print(f"O menor peso foi {leve:.2f}kg. Pessoa mais leve:")
for pessoa in lista_total:
    if pessoa[1] == leve:
        print(f" - [{pessoa[0]}]")
