a1 = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razão: "))
termo = a1
contador = 0
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador < total:
        print("{}".format(termo), end = " -> ")
        termo += r
        contador += 1
    print("Pausa")
    mais = int(input("Quanto termos a mais, você quer mostrar? "))
print("Fim")
