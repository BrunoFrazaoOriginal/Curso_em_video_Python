n = 0
contador = 0
soma = 0
while n != 999:
    n = int(input("Digite um número qualquer, caso queira parar, digite 999: "))
    if n != 999:
        contador += 1
        soma += n
print("Você digitou {} números e a soma deles é igual a {}.".format(contador, soma))
