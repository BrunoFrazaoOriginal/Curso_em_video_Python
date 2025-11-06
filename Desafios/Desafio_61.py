a1 = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razão: "))
termo = a1
contador = 0
while contador < 10:
    print("{}".format(termo), end = " -> ")
    termo += r
    contador += 1
print("Fim")
