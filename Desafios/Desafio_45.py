from random import randint
itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)
print("""Suas opções são:
      [0] Pedra
      [1] Papel
      [2] Tesoura""")
jogador = int(input("Qual é a sua jogada? "))
if computador == 0: # computador jogou Pedra
    if jogador == 0:
        print("Empate")
    elif jogador == 1:
        print("Jogador Vence")
    elif jogador == 2:
        print("Computador Vence")
    else:
        print("Jogada inválida")
elif computador == 1: # computador jogou Papel
    if jogador == 0:
        print("Computador Vence")
    elif jogador == 1:
        print("Empate")
    elif jogador == 2:
        print("Jogador Vence")
    else:
        print("Jogada inválida")
elif computador == 2: # computador jogou Tesoura
    if jogador == 0:
        print("Jogador Vence")
    elif jogador == 1:
        print("Computador Vence")
    elif jogador == 2:
        print("Empate")
    else:
        print("Jogada inválida")

print("O computador escolheu {}".format(itens[computador]))
