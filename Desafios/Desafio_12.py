nome = str(input("Qual o nome do produto? "))
p = float(input("Qual o preço do produto? R$"))
d = p-(p*0.05)
print("Uma unidade do produto {} custa R${}, mas com 5% de desconto, o preço será de R${:.2f}.".format(nome, p, d))
