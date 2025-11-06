from datetime import date

#def voto():
    #data = int(input("Digite o ano de nascimento: "))
    #nasc = datetime.today().year - data
    #if nasc < 16:
    #    print(f"Você tem {nasc} anos, ainda não pode votar.")
    #if 16 <= nasc < 65:
    #    print(f"Você tem {nasc} anos e pode votar.")
    #else: 
    #    if nasc >= 65:
    #        print(f"Você tem {nasc} anos, o seu voto é opcional.")
    

#voto()

def voto(ano):
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f"Com {idade} anos: Ainda não vota."
    elif 16 <= idade < 18 or idade > 65:
        return f"Com {idade} anos: O voto é opcional."
    else:
        return f"Com {idade} anos: O voto é obrigatório."
    

nasc = int(input("Qual a data de nascimento? "))
print(voto(nasc))