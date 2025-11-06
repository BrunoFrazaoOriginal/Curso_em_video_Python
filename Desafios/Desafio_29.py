velocidade_carro = float(input("Qual a velocidade do carro (em km/h)? "))
if velocidade_carro > 80:
    print("Você ultrapassou o limite de velocidade e será multado!")
    excesso = velocidade_carro - 80
    multa = excesso * 7
    print("Você deverá pagar R${} de multa!".format(multa))
else:
    print("Você está dentro do limite de velocidade! Boa viagem!")
