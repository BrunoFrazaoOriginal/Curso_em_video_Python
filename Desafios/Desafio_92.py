from datetime import date
dados = {}
data = date.today().year

dados["Nome"] = str(input("Digite o nome da pessoa: ")).strip().upper()
dados["Nascimento"] = int(input("Digite o ano de nascimento da pessoa: "))
dados["CTPS"] = int(input("Digite o numero da carteira de trabalho, da pessoa: "))

if dados["CTPS"] == 0:
    print(dados)
else: 
    if dados["CTPS"] > 0:
        contratação = int(input("Qual o ano de contratação da pessoa? "))
        salário = float(input("Qual o salário da pessoa? R$"))
idade = data - dados["Nascimento"]
aposentar = idade + (35 - (data - contratação))
dados["Idade"] = idade
dados["Aposentadoria"] = aposentar
dados["Contratação"] = contratação
dados["Salário"] = salário  
print(f"O funcionário {dados["Nome"]}, nasceu em {dados["Nascimento"]}, tem {dados["Idade"]} anos, CTPS de Nº{dados["CTPS"]}, foi contratado em {dados["Contratação"]}, recebendo R${dados["Salário"]}, e irá se aposentar com {dados["Aposentadoria"]} anos.")

