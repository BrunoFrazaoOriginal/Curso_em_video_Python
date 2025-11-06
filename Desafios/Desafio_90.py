aluno = {}
alunos = []
while True:
    aluno["Nome"] = str(input("Qual o nome do(a) aluno(a): ")).strip().upper()
    aluno["Média"] = float(input("Qual a média do(a) aluno(a): "))
    alunos.append(aluno.copy())

    continuar = str(input("Deseja cadastrar mais um(a) aluno(a)? [S/N] ")).strip().upper()[0]
    while continuar not in "SN":
        continuar = str(input("Deseja cadastrar mais um(a) aluno(a)? [S/N] ")).strip().upper()[0]
    if continuar == "N":
        break

print("==" * 30)
for m in alunos:        
    if m["Média"] >= 7:
        print(f"Aluno(a) {m["Nome"]}, conseguiu média de 7 ou mais e está aprovado(a)!")
    else:
        print(f"Aluno(a) {m["Nome"]}, não conseguiu média de 7 ou mais e está reprovado(a)!"),
print("==" * 30)