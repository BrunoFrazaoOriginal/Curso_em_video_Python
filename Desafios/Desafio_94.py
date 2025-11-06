pessoas = {}
mulheres = []
acima = []
lista = []
qtd_pessoas = média = total_idade = 0
while True:
    pessoas["nome"] = str(input("Qual o nome da pessoa? ")).strip().upper()
    pessoas["gênero"] = str(input("Qual o gênero da pessoa? [M/F] ")).strip().upper()[0]
    while pessoas["gênero"] not in "MF":
        print("Opção de gênero inválida! Diga M para masculino ou F para feminino.")
        pessoas["gênero"] = str(input("Qual o gênero da pessoa? [M/F] ")).strip().upper()[0]
    pessoas["idade"] = int(input("Qual a idade da pessoa? "))
    lista.append(pessoas.copy())
    qtd_pessoas += 1
    total_idade += pessoas["idade"]

    if pessoas["gênero"] == "F":
        mulheres.append(pessoas["nome"])
    
    continuar = str(input("Deseja cadastrar outra pessoa? [S/N] ")).strip().upper()[0]
    while continuar not in "SN":
        if continuar != "S":
            print("Opção inválida! Escolha S para continuar ou N para encerrar.")
            continuar = str(input("Deseja cadastrar outra pessoa? [S/N] ")).strip().upper()[0]
    if continuar == "N":
        break

média = total_idade / qtd_pessoas
for p in lista:
    if p["idade"] > média:
        acima.append(p["nome"])
       
print("-=" * 30)
print(lista)
print("-=" * 30)
print(f"Foram cadastradas {qtd_pessoas} pessoas.")
print("-=" * 30)
print(f"A média de idade das pessoas cadastradas, é de {média:.2f} anos.")
print("-=" * 30)
print(f"As mulheres cadastradas, são: {mulheres}.")
print("-=" * 30)
print(f"As pessoas que estão acima da média, são: {acima}.")
print("-=" * 30)
