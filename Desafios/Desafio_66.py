n = contador = soma = 0
while True:
    n = int(input("Digite um número inteiro qualquer, caso queira parar, digite 999: "))
    if n == 999:
        break
    elif n != 999:
        contador += 1
        soma += n
print(f"Você digitou {contador} números e a soma entre eles é igual a {soma}.")
