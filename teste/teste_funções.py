def pessoa(nome):
    print("-=" * 30)
    print(nome)
    print("-=" * 30)


pessoa("Bruno")


def matematica(numeros):
    print("-=" * 30)
    print(numeros)
    print("-=" * 30)


matematica(30)


def contador(* num):
    for valor in num:
        print(f"{valor} ", end="")
    print("Fim")


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)


def contador(* núm):
    tam = len(núm)
    print(f"Recebi os valores {núm} e são ao todo {tam} números.")


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)


def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos +=1

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)


def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f"Somando os valores {valores} temos {s}.")


soma(5, 2)
soma(2, 9, 4)