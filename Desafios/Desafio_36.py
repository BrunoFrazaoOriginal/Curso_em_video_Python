valor = float(input("Informe o valor da casa: R$"))
salário = float(input("Informe o valor do seu salário: R$"))
anos = int(input("Informe por quantos anos você vai pagar, essa casa (em meses): "))
prestação = valor / anos 
print("O valor da prestação, será de R${:.2f}.".format(prestação))

if prestação > salário * 30 / 100:
    print("Parabéns! O seu empréstimo imobiliário foi aprovado!")
else:
    print("O seu empréstimo foi negado. Você pode tentar novamente, com outros valores e condições.")
    
