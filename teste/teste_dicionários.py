#pessoas = {"nome": "Bruno", "gênero": "Masculino", "idade": 39}
#pessoas["peso"] = 130
#print(f"O {pessoas["nome"]} é do gênero {pessoas["gênero"]} e tem {pessoas["idade"]} anos.")
#print(pessoas.keys())
#print(pessoas.values())
#print(pessoas.items())
#for k in pessoas.keys():
    #print(k)
#for k in pessoas.values():
    #print(k)
#for k in pessoas.items():
    #print(k)
#for k, v in pessoas.items():
    #print(f"{k} = {v}")

#brasil = []
#estado1 = {"UF": "Rio de Janeiro", "Sigla": "RJ"}
#estado2 = {"UF": "São Paulo", "Sigla": "SP"}
#brasil.append(estado1)
#brasil.append(estado2)
#print(brasil[0]["UF"])
#print(brasil[1]["Sigla"])

estado = {} #Dicionário
brasil = [] #Lista
for e in range(0, 3):
    estado["UF"] = str(input("Unidade Federativa: ")).strip().upper()
    estado["Sigla"] = str(input("Sigla do estado: ")).strip().upper()
    brasil.append(estado.copy())
for l in brasil:
    for v in l.values():
        print(v, end=" ")
    print()

