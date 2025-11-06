base = 1250
salário = float(input("Qual o valor do seu salário? R$"))
if salário > base:
    aumento1 = salário * 0.10 + salário
    print("Com o aumento, o seu novo salário será de: R${:.2f}".format(aumento1))
if salário <= base:
    aumento2 = salário * 0.15 + salário
    print("Com o aumento, o seu novo salário será de: R${:.2f}".format(aumento2))
