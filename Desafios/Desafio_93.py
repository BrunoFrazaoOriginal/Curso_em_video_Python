gols = 0
jogador = {}
jogador["Nome"] = str(input("Qual o nome do jogador? ")).strip().upper()
jogador["Partidas"] = int(input(f"Em quantas partidas {jogador['Nome']} atuou? "))
for g in range(jogador["Partidas"]):
    gols_partida = int(input(f"Quantos gols o jogador fez na {g+1}º partida? "))
    gols += gols_partida
jogador["gols"] = gols_partida
print("-=" * 30)
print(jogador)
print("-=" * 30)
print(f"O jogador {jogador["Nome"]}, jogou {jogador["Partidas"]} e ao todo fez {gols} gols, no campeonato.")
print("-=" * 30)
