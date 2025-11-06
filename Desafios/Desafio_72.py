numeros = ("zero", "um", "dois", "três", "quatro", 
           "cinco", "seis", "sete", "oito", "nove", 
           "dez", "onze", "doze", "treze", "catorze", 
           "quinze", "dezesseis", "dezessete", "dezoito", 
           "dezenove", "vinte")

while True:
    escolha = int(input("Escolha um número de 0 a 20: "))

    if 0 <= escolha <= 20:
        print(f"Você escolheu {numeros[escolha]}")
        break
    else:
        print("Opção inválida! Escolha entre 0 e 20.")
print("Fim do programa")