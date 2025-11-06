nome = str(input("Digite o seu nome completo: ")).strip()
print("Seu nome em maiúsculas é: ", (nome.upper()))
print("Seu nome em minúsculas é: ", (nome.lower()))
print("A quantidade de caracteres do seu nome, é: ", (len(nome) - nome.count(" ")))
primeiro = nome.split()
print("A quantidade de caracteres do seu primeiro nome, é: ", (len(primeiro[0])))


