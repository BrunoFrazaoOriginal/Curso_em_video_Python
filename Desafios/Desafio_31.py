passagem = float(input("Qual a distância da sua viagem (em km)? "))
if passagem <= 200:
    valor = passagem * 0.5
    print("O valor da sua passagem, será de R${}.".format(valor))
else:
    valor_acima = passagem * 0.45
    print("O valor da sua passagem, será de R${}.".format(valor_acima))
