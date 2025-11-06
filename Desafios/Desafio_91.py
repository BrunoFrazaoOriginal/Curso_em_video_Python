from random import randint
from time import sleep
from operator import itemgetter

jogadas = {"Jogador1": randint(1, 6),
            "Jogador2": randint(1, 6),
            "Jogador3": randint(1, 6),
            "Jogador4": randint(1, 6)
            }
ranking = []
print(jogadas)
for k, v in jogadas.items():
    print(f"{k} tirou {v} no dado.")
    sleep(1)
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
print("-=" * 30)
print("===== Ranking dos Jogadores =====")
for i, v in enumerate(ranking):
    print(f"{i+1}º Lugar: {v[0]} com {v[1]}.")
    sleep(1)