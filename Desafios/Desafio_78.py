valores = []
for cont in range(0, 5):
    valores.append(int(input(f"Digite um valor inteiro para a posição {cont}: ")))
maior = menor = valores[0]
for c, v in enumerate(valores):
    print(f"O número {v} está na posição {c} da lista.")
    if v > maior:
        maior = v
    if v < menor:
        menor = v
print(f"A lista de valores digitados, foi: {valores}.")
print(f"Dentre os valores digitados, {maior} é o maior, e {menor} é o menor.")
print("Fim do programa")