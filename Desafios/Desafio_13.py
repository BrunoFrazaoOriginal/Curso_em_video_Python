s = float(input("Qual o salário do funcionário? R$"))
a = s+(s*0.15)
print("O funcionário passará a receber R${:.2f}, devido ao aumento de 15% sobre o salário anterior, de R${:.2f}.".format(a, s))
