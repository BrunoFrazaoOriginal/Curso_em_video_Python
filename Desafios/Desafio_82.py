lista_total = []
lista_par = []
lista_impar = []
while True:
    numero = int(input("Digite um número: "))
    lista_total.append(numero)
    if numero % 2 == 0:
        lista_par.append(numero)
    if numero % 2 == 1:
        lista_impar.append(numero)
    continuar = str(input("Deseja digitar outro número? [S/N] ")).strip().upper()[0]
    while continuar not in "SN":
        print("Opção inválida! Digite S para continuar ou N para parar.")
        continuar = str(input("Deseja digitar outro número? [S/N] ")).strip().upper()[0]
    if continuar == "N":
        break
print(f"A lista com todos os números é: {lista_total}.")
print(f"A lista com os números pares é: {lista_par}.")
print(f"A lista com os números ímpares é: {lista_impar}.")
    
