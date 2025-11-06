from random import randint
tupla = ()
maior = menor = 0
for n in range(0, 5):
    numero = randint(1, 10)
    tupla += (numero, )
    if maior == 0 or numero > maior:
        maior = numero
    if menor == 0 or numero < menor:
        menor = numero
print(f"Os números sorteados, são: {tupla}")
print(f"O maior número sorteado é: {maior}")
print(f"O menor número sorteado é: {menor}")

