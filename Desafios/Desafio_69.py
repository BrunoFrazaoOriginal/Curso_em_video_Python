acima_18 = homens = mulheres_menos_20 = 0
while True:
    gênero = ""
    while gênero not in ("M", "F"):
        gênero = str(input("Qual o seu gênero? [M/F] ")).strip().upper()[0]
        if gênero not in ("M", "F"):
                print("Opção Inválida! Escolha M ou F.")
    idade = int(input("Qual a sua idade? "))
    if gênero == "F" and idade < 20:
            mulheres_menos_20 += 1
    if gênero == "M":
            homens += 1
    if idade >= 18:
            acima_18 += 1
    print("-=" * 20)
    print("Dados registrados.")
    print("""
    [S] Sim
    [N] Não
    """)
    print("-=" * 20)
    opção = str(input(">>>>>>> Deseja cadastrar outra pessoa? [S/N] ")).strip().upper()
    if opção != "S":
        break
print(f"Ao todo temos {acima_18} pessoas com mais de 18 anos, além de {homens} homens cadastrados e por último temos {mulheres_menos_20} mulheres com menos de 20 anos cadastradas.")
print("Fim do programa")
