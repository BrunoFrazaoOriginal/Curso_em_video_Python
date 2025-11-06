import sys
import os

# Garante que a pasta raiz (onde está 'modulos') esteja no caminho de import
sys.path.append(os.path.dirname(os.path.dirname(__file__)))


from modulos import moeda

valor = float(input("Digite o preço: R$"))
print(f"A metade de R${valor} é R${moeda.metade(valor)}.")
print(f"O dobro de R${valor} é R${moeda.dobro(valor)}.")
print(f"Aumentando R${valor} em 10%, temos R${moeda.aumentar(valor)}.")
print(f"Reduzindo R${valor} em 10%, temos R${moeda.diminuir(valor)}")