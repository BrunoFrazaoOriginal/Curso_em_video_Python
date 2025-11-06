import math
cateto = float(input("Digite o comprimento do cateto: "))
catetad = float(input("Digite o comprimento do cateto adjacente: "))
hipotenusa = math.hypot(cateto, catetad)
print("O comprimento da hipotenusa, é: {:.2f}.".format(hipotenusa))
