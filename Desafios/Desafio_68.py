from random import randint
vitorias = 0
escolha = " "
while True:
    jogada_pc = randint(1, 11)
    jogador = int(input("Escolha um número inteiro: "))
    resultado = jogada_pc + jogador
    escolha = ""
    while escolha not in ("P", "I"):
        escolha = str(input("Tenta adivinhar se o número escolhido é par ou ímpar [P/I]: ")).strip().upper()[0]
        if escolha not in ("P", "I"):
            print("Opção inválida! Tente novamente.")
    if escolha == "P":
        if resultado % 2 == 0:
            print(f"O computador escolheu {jogada_pc} e você escolheu {jogador}, e {jogada_pc} + {jogador} = {jogada_pc + jogador}, que é Par. Você ganhou!")
            vitorias += 1
        else:
            print(f"O computador escolher {jogada_pc} e você escolheu {jogador}, e {jogada_pc} + {jogador} = {jogada_pc + jogador}, que não é Par. Você Perdeu!")
            break
    elif escolha == "I":
        if resultado % 2 == 1:
            print(f"O computador escolheu {jogada_pc} e você escolheu {jogador}, e {jogada_pc} + {jogador} = {jogada_pc + jogador}, que é Ímpar. Você ganhou!")
            vitorias += 1
        else:
            print(f"O computador escolheu {jogada_pc} e você escolheu {jogador}, e {jogada_pc} + {jogador} = {jogada_pc + jogador}, que não é Ímpar. Você Perdeu!")
            break
print(f"Fim de jogo! Você teve {vitorias} vitórias consecutivas!")
