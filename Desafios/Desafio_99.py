from time import sleep
def maior():
    maior = 0
    while True:
        numero = int(input("Digite um valor inteiro (999 para parar): "))
        if numero == 999:
            break
   

    
        if maior == 0 or numero > maior:
            maior = numero
        if maior != 999:
            maior = numero
        if numero == 0:
            maior = numero
    sleep(1)
    print(f"Dentre os parametros digitados, o maior é {maior}.")


maior()
