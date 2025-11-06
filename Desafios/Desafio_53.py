frase = str(input("Digite uma frase: ")).strip().lower()
frase = frase.replace(" ", "")
inverso = ""

for i in range(len(frase) -1, -1, -1):
    inverso += frase[i]

if frase == inverso:
    print("A frase '{}' é um palíndromo!".format(frase))
else:
    print("A frase '{}', não é um palíndromo!".format(frase))
