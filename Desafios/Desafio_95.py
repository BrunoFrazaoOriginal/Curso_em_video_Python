jogadores = {}
players = []
while True:
    jogadores.clear()
    jogadores["Nome"] = str(input("Qual o nome do jogador? ")).strip().upper()
    jogadores["Partidas"] = int(input("Em quantas partidas ele atuou? "))

    gols = []

    for g in range(jogadores["Partidas"]):
        gols_partida = int(input(f"Quantos gols o jogador fez na {g+1}º partida? "))
        gols.append(gols_partida)
    
    jogadores["gols"] = gols[:]
    jogadores["total"] = sum(gols)

    players.append(jogadores.copy())

    continuar = str(input("Quer incluir um outro jogador? [S/N] ")).strip().upper()[0]
    while continuar not in "SN":
        if continuar != "S":
            print("Opção inválida! Escolha S para continuar ou N para sair.")
            continuar = str(input("Quer incluir um outro jogador? [S/N] ")).strip().upper()[0]
    if continuar == "N": 
        break
for i, j in enumerate(players):
    print(f"{i:<4}{j['Nome']:<15}{str(j['gols']):<20}{j['total']:<6}")
print("-=" * 30)
while True:
    dados = int(input("Mostrar dados de qual jogador? (999 para parar): "))
    if dados == 999:
        break
    if dados >= len(players):
        print(f"ERRO! Não existe jogador associado a esse número em {dados}.")
    else:
        print(f" -- Levantamento do jogador {players[dados]['Nome']}:")
        for i, g in enumerate(players[dados]['gols']):
            print(f"  No jogo {i+1} fez {g} gols.")
print("-=" * 30)

 
