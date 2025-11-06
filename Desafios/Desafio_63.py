n = int(input("Digite um número: "))
a, b = 0, 1
contador = 0
print("A sequencia de Fibonacci, é: ", end=" -> ")
while contador < n:
    print(a, end=" ")
    a, b = b, a + b
    contador += 1
print("Fim da sequencia.")
