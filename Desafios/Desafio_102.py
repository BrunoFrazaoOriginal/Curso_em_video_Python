def fatorial(num, show=False):
    """
    -> calcula o fatorial de um número.
    parametro num: O número a ser calculado.
    parametro show: (opcional) Mostrar ou não o processo de cálculo.
    return: O valor do fatorial de num.
    """
    f = 1
    for c in range(num, 0, -1):
        f*= c
        if show:
            print(c, end=" ")
            if c > 1:
                print("x", end=" ")
            else:
                print("=", end=" ")
    return f


num = int(input("Digite um número para calcular o fatorial: "))

mostrar = str(input("Deseja mostrar o processo? [S/N] ")).strip().upper()[0]
while mostrar not in "SN":
    print("Opção inválida! Escolha S para mostrar o cálculo, ou N para não mostrar.")
    mostrar = str(input("Deseja mostrar o processo? [S/N] ")).strip().upper()[0]
    if mostrar == "S":
        mostrar = True
    else:
        mostrar = False
print(fatorial(num, show=mostrar))
