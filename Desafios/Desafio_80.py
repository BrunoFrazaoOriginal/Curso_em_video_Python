lista = []
for n in range(0,5):
    numero = int(input("Digite um número: "))
    if n == 0 or numero > lista[-1]:
        lista.append(numero)
    else:
        posicao = 0
        while posicao < len(lista):
            if numero <= lista[posicao]:
                lista.insert(posicao, numero)
                break
            posicao += 1
print("-=" * 30)
print(f"Os números digitados, já em ordem crescente, são: {lista}")
