while True:
    numero = int(input("Digite um número inteiro, negativo para parar: "))
    if numero < 0:
        break
    print("-" * 20)
    for n in range (1, 11):
        tabuada = numero * n
        print(f"{numero} x {n} = {tabuada}")
    print("-" * 20)
print("Fim das tabuadas.")
