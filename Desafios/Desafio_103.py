def ficha(nome="<desconhecido>", gols=0):
    """
    -> Exibe a ficha de um jogador
    parametro nome: nome do jogador (opcional)
    parametro gols: número de gols marcados (opcional)
    return: nenhum
    """
    print(f"O jogador {nome} fez {gols} gol(s) no campeonato.")


nome = str(input("Digite o nome do jogador: ")).strip().upper()
gols = input("Digite quantos gols ele marcou: ").strip()


if gols == "":
    gols = 0
else: 
    gols = int(gols)


if nome == "":
    nome = "<desconhecido>"

ficha(nome, gols)