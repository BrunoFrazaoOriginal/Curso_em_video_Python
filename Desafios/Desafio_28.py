import random
numero_secreto = random.randint(0, 5)

tentativa = int(input("Tente adivinhar o número secreto, entre 0 a 5: "))
if tentativa == numero_secreto:
    print("Parabéns! Você acertou!")
else:
    print("Você errou! O número era {}. Tente novamente.".format(numero_secreto))
