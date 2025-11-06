from time import sleep
n = int(input("Digite um número para calcular o seu fatorial: "))

fatorial = 1
contador = n
print("Calculando {}! ".format(n))
sleep(1)
print(".")
sleep(1)
print(".")
sleep(1)
print(".")
sleep(1)
while contador > 0:
    fatorial *= contador
    contador -= 1

print("O fatorial de {} é {}.".format(n, fatorial))
