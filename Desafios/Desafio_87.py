matriz = [[], [], []]
soma_par = maior_lin2 = soma_col3 = 0

for linha in range(3):
    for coluna in range(3):
        valor = int(input(f"Digite um valor para [{linha}, {coluna}]: "))
        matriz[linha].append(valor)

print("\nMatriz 3x3:")
for linha in matriz:
    for valor in linha:
        print(f"[{valor:^5}]", end="")
    print()

for linha in range(3):
    for coluna in range(3):
        valor = matriz[linha][coluna]

        if valor % 2 == 0:
            soma_par += valor
        
        if coluna == 2:
            soma_col3 += valor
maior_lin2 = matriz[1][0]
for coluna in range(1, 3):
    if matriz[1][coluna] > maior_lin2:
        maior_lin2 = matriz[1][coluna]

print(f"A soma de todos os pares, é: {soma_par}")
print(f"A soma dos valores da terceira coluna, é: {soma_col3}")
print(f"O maior valor da segunda linha, é: {maior_lin2}")