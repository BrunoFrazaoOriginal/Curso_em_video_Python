nome = str(input("Qual o seu nome? ")).strip()
print("Muito prazer, {}!".format(nome))
print("O seu primeiro nome é: {}".format(nome.split()[0]))
print("O seu último nome é: {}".format(nome.split()[-1]))
