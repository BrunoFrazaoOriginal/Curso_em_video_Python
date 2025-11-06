peso = float(input("Digite o seu peso (kg): "))
altura = float(input("Digite a sua altura (m): "))
imc = peso / altura ** 2
if imc < 18.5:
    print("O seu IMC é de {:.2f}, você está abaixo do peso ideal.".format(imc))
elif 18.5 <= imc < 25:
    print("O seu IMC é de {:.2f}, você está no seu peso ideal.".format(imc))
elif 25 <= imc < 30:
    print("O seu IMC é de {:.2f}, você está acima do seu peso ideal, se cuide mais.".format(imc))
elif 30 <= imc < 40:
    print("O seu IMC é de {:.2f}, você está obeso, procure se cuidar melhor.".format(imc))
else:
    print("O seu IMC é de {:.2f}, você está com obesidade mórbida, a sua vida está em risco, procure ajuda!".format(imc))
