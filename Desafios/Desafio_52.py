n = int(input("Digite um número: "))
primo = True

if n <= 1:
    primo = False
else:
    for i in range(2, n):
        if n % i == 0:
            primo = False
if primo:
    print("O número {}, é um número primo.".format(n))
else:
    print("O número {}, não é um número primo.".format(n))

