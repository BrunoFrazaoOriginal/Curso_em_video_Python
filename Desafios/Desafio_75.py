tupla = ()
pares = ()
contador_9 = 0
for n in range(0, 4):
    numero = int(input("Digite um número inteiro: "))
    tupla += (numero, )
    if numero == 9:
        contador_9 +=1
    if numero % 2 == 0:
        pares += (numero, )
if 3 in tupla:
    print(f"O número 3 apareceu na posição: {tupla.index(3)+1}")
else:
    print("O número 3 não apareceu em nenhuma posição.")
print(f"Os números digitados, foram: {tupla}")
print(f"O número 9 foi digitado {contador_9} vezes.")

