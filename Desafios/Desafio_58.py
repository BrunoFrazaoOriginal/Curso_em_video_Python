from random import randint
numero_secreto = randint(0, 10)
contador = 0
acertou = False
while not acertou:
    tentativa = int(input("Tente adivinhar o número secreto, entre 0 e 10: "))
    contador += 1
    if tentativa == numero_secreto:
        acertou = True
    else:
        if tentativa < numero_secreto:
            print("Quase lá! Tente novamente com um número maior.")
        elif tentativa > numero_secreto:
            print("Quase lá! Tente novamente com um número menor.")
print("Parabéns! Você acertou!")
print("Você levou {} tentativas para acertar.".format(contador))
