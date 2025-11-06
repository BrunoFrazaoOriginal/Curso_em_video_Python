total_gasto = produtos = 0
barato = None
nome_barato = ""
while True:
    produto = str(input("Digite o nome do produto: ")).strip().upper()
    preço = float(input("Digite o preço do produto: R$"))
    if preço > 1000:
        produtos += 1
    if barato is None or preço < barato:
        barato = preço
        nome_barato = produto
    total_gasto += preço
    while True:
        continuar = str(input("Deseja cadastrar um novo produto? [S/N] ")).strip().upper()
        if continuar in ("S", "N"):
            break
        print("Opção Inválida! Digite apenas S ou N.")
    if continuar == "N":
            break
print("-=" *50)
print(f"O total de gastos dessa compra, é de R${total_gasto}.")
print(f"{produtos} tem mais de R$1000.")
print(f"O produto {nome_barato}, é o mais barato.")
