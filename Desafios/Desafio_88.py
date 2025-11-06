from random import randint
from time import sleep
jogadas = []
print("-=" * 30)
qtd_listas = int(input("Quatos jogos você quer gerar? "))
print("-=" * 30)
for p in range(qtd_listas):
    jogada = []
    while len(jogada) < 6:
        numeros = randint(1, 60)
        if numeros not in jogada:
            jogada.append(numeros)
    jogadas.append(jogada)
print(f"Você escolheu gerar {qtd_listas} jogos.")
for p, sub in enumerate(jogadas, start=1):
    print(f"O {p}º jogo, é: {sub}")
    sleep(1)
print("-=" * 12, "BOA SORTE!", "-=" * 12)