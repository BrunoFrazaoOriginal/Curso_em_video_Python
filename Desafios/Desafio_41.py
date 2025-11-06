from datetime import date
hoje = date.today().year
ano = int(input("Em que ano o atleta nasceu? "))
idade = hoje - ano
print("O atleta tem {} anos de idade.".format(idade))
if idade <= 9:
    print("Esse atleta é da categoria MIRIM.")
elif 9 < idade <= 14:
    print("Esse atleta é da categoria INFANTIL.")
elif 14 < idade <= 19:
    print("Esse atleta é da categoria JUNIOR.")
elif 19 < idade <= 25:
    print("Esse atleta é da categoria SÊNIOR.")
else:
    print("Esse atleta é da categoria MASTER.")
