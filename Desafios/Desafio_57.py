sexo = str(input("Digite o sexo da pessoa [M/F]: ")).strip().upper()[0]
while sexo not in ("M", "m", "F", "f"):
    sexo = str(input("Opção incorrteta, digite o sexo da pessoa [M/F]: ")).strip().upper()[0]
    if sexo not in ("M", "F"):
        print("Você digitou {}, opção inválida.".format(sexo))
    else:
        print("Você digitou {}, opção correta.".format(sexo))
print("Fim")
