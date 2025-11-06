preco_normal = float(input("Qual o preço normal do produto? R$"))
print('''Formas de pagamento
      [1] à vista (Dinheiro, Pix)
      [2] à vista (Cartão)
      [3] 2x no cartão
      [4] 3x ou mais no cartão''')
opção = int(input("Qual a forma de pagamento? "))
if opção == 1:
    desconto = preco_normal - (preco_normal *10 /100)
    print("O preço do produto com 10% de desconto é R${:.2f}.".format(desconto))
elif opção == 2:
    desconto = preco_normal - (preco_normal *5 /100)
    print("O preço do produto com 5% de desconto é R${:.2f}.".format(desconto))
elif opção == 3:
    parcela = preco_normal / 2
    print("O preço do produto é R${:.2f}, dividio em 2x de R${:.2f}.".format(preco_normal, parcela))
elif opção == 4:
    total = int(input("Quantas parcelas? "))
    juros = preco_normal + (preco_normal * 20 / 100)
    parcela = juros / total
    print("O preço do produto com 20% de juros é R${:.2f}, dividio em {}x de R${:.2f}.".format(juros, total, parcela))