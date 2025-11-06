from datetime import date
nascimento = int(input("Informe a data de nascimento: "))
data_atual = date.today().year
idade = data_atual - nascimento
print("Quem nasceu em {} tem {} anos em {}.".format(nascimento, idade, data_atual))
if idade == 18:
    print("Está na hora de se alistar!")
elif idade > 18:
    print("Já passou da hora de se alistar! Se apresente logo!")
elif idade < 18:
    saldo = 18 - idade
    print("Ainda não está na hora de se alistar. Faltam {} anos para o alistamento.".format(saldo))

