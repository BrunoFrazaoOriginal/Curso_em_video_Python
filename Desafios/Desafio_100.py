from random import randint
from time import sleep

def sorteio():
    print("Os números sorteados, foram: ", end=" ")
    for n in range(0, 5):
        numeros = randint(1, 10)
        sorteados.append(numeros)
        print(f"{numeros}", end=" ", flush=True)
        sleep(1)
    print("Fim!")


def somaPAR():
    soma = 0
    for n in sorteados:
        if n % 2 == 0:
            soma += n
    print(f"A soma dos valores pares, é: {soma}.")

sorteados = []
sorteio()
sleep(2)
somaPAR()