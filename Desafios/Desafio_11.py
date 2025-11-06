n1 = float(input("Qual a largura da parede? "))
n2 = float(input("Qual a altura da parede? "))
area = n1*n2
litros = area/2
print("Para uma parede com {} metros de largura e {} metros de altura, será necessário utilizar {:.2f} litros de tinta, por ter uma area de {:.2f}m².".format(n1, n2, litros, area))
