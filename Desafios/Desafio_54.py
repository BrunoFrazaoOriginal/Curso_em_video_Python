from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for n in range(0, 7):
    ano = int(input("Qual o ano do seu nascimento? "))
    idade = atual - ano
    if idade < 18:
        totmenor += 1
        print("Você tem {} anos e ainda não atingiu a maioridade.".format(idade))
    else:
        totmaior += 1
        print("Você tem {} anos, e já atingiu a maioridade.".format(idade))
print("Ao todo tivemos {} pessoas maiores de idade, e {} pessoas menores de idade.".format(totmaior, totmenor))
print("Fim.")
