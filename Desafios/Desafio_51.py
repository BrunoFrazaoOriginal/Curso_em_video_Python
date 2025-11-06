a1 = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razão: "))
n = int(input("Quantos termos você quer mostrar? "))
print("A progressão aritmética, será:")
for p in range(n):
    termo = a1 + p * r
    print("{}".format(termo), end=" -> ")
print("Fim")
