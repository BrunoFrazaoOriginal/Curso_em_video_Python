#help(print)
#help(len)
#help(input)
#help(str)


#def contador(i, f, p):
#    """
#    -> Faz uma contagem e mostra na tela.
#    parametro i: início da contagem
#    parametro f: fim da contagem
#    parametro p: passo da contagem
#    return: sem retorno
#    """
#    c = i
#    while c <= f:
#        print(f"{c}", end="..")
#        c += p
#    print("Fim!")


#contador(2, 10, 2)


#def somar(a=0, b=0, c=0):
#    s = a + b + c
#    print(f"A soma de {a} + {b} + {c} é igual a {s}")


#somar(5, 6, 9)
#somar(c=5, a=8, b=7)


#def teste():
#    x = 8
#    print(f"Na função teste, n vale {n}.")
#    print(f"Na função teste, x vale {x}.")


# Programa Principal
#n = 2
#print(f"No programa principal, n vale {n}")
#teste()
# print(f"No programa principal, x vale{x}.") Não funciona pois x é uma variável local, dentro da função, enquanto que n é uma variável global, funcionando no programa todo.


#def teste(b):
#    global a  # Faz o A usar o valor de dentro para a global, apagando o valor de fora.
#    a = 8
#    b += 4
#    c = 2
#    print(f"A dentro vale {a}.")
#    print(f"B dentro vale {b}.")
#    print(f"C dentro vale {c}.")

#a = 5
#teste(a)
#print(f"A fora vale {a}.")
#print(f"B fora vale {b}.") Não funcionam
#print(f"C fora vale {c}.") Não funcionam


#def somar(a=0, b=0, c=0):
#    s= a + b + c
#   return s


#r1 = somar(3, 2, 5)
#r2 = somar(2, 2)
#r3 = somar(7)

#print(f"Os resultados, foram: {r1}, {r2}, {r3}.")


#def fatorial(num=1):
#    f = 1
#    for c in range(num, 0, -1):
#        f *= c
#    return f


#n = int(input("Digite um número: "))
#print(f"O fatoral de {n} é igual a {fatorial(n)}")


#f1 = fatorial(5)
#f2 = fatorial(4)
#f3 = fatorial(1)

#print(f"Os resultados das fatorias, são: {f1}, {f2}, {f3}.")


#def par(n=0):
#    if n % 2 == 0:
#        return True
#    else:
#        return False
    

#num = int(input("Digite um número: "))
#print(par(num))
#if par(num):
#    print(f"{num} é par!")
#else:
#    print(f"{num} é ímpar!")

def calculo_soma(a=0, b=0, c=0):
    resultado = a + b + c
    return resultado


soma1 = calculo_soma(5, 10, 15)
soma2 = calculo_soma(10, 15)
soma3 = calculo_soma(5)
print(f"A primeira soma da {soma1}, a segunda dá {soma2} e a terceira dá {soma3}.")