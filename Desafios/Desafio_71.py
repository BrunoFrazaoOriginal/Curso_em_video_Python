from time import sleep
print("{:^50}".format(" Bando DEV "))
sleep(2)
print("-=" * 50)
saque = int(input("Qual o valor a ser sacado? R$"))
print("-=" * 50)
sleep(3)
maior = 50
totmaior = 0
total = saque

while True:
    if total >= maior:
        total -= maior 
        totmaior += 1
    else:
        if totmaior > 0:
            print(f"Sacando R${saque}, em {totmaior} cédulas de R${maior}.")
        if maior == 50:
            maior = 20
        elif maior == 20:
            maior = 10
        elif maior == 10:
            maior = 1
        totmaior = 0
        if total == 0:
            break
print("-=" *50)
print("Obrigado por usar os nossos serviços, volte sempre.")