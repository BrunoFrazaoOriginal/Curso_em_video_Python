pessoas = int(input("Quantas pessoas serão analisadas? "))
soma = 0
homem_velho = ""
idade_homem_velho = 0
mulheres_menor_20 = 0
for n in range(pessoas):
    print("----------- {}ª Pessoa -------------".format(n+1))
    nome = str(input("Qual o nome da {}ª pessoa? ".format(n+1))).strip().upper()
    idade = int(input("Qual a idade da {}ª pessoa? ".format(n+1)))
    sexo = str(input("Qual o sexo da {}ª pessoa? [M/F] ".format(n+1))).strip().upper()
    soma += idade
    media = soma / pessoas
    if sexo == "M":
       if idade > idade_homem_velho:
           idade_homem_velho = idade
           homem_velho = nome
    if sexo == "F" and idade < 20:
        mulheres_menor_20 += 1
print("A média de idade do grupo é {} anos.".format(media))
print("O nome do homem mais velho é {}, que tem {} anos.".format(homem_velho, idade_homem_velho))
print("E por último, {} mulher(es) tem menos de 20 anos.".format(mulheres_menor_20))
