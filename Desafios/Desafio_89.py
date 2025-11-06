boletim = []
while True:
    nome = str(input("Digite o nome do aluno: ")).strip().upper()
    n1 = float(input("Digite a nota da primeira prova: "))
    n2 = float(input("Digite a nota da segunda nota: "))
    boletim.append([nome, n1, n2])
    continuar = str(input("Deseja colocar as notas de outro aluno? [S/N] ")).strip().upper()[0]
    while continuar not in "SN":
        print("Opção inválida! Escolha S para cadastrar um outro aluno, ou N para sair.")
        continuar = str(input("Deseja colocar as notas de outro aluno? [S/N] ")).strip().upper()[0]
    if continuar == "N":
        break
print("====" * 20)
print("\nO boletim da turma:")
média = (n1 + n2) / 2
for aluno in boletim:
    print("-=" * 50)
    print(f"Aluno(a): {aluno[0]:<30} - Nota 1: {aluno[1]:>2} - Nota 2: {aluno[2]:>2}, Média {média:>2}")
    if média >= 7:
        print("Aluno(a) APROVADO(A)!")
        print("-=" * 50)
    else:
        print("Aluno(a) REPROVADO(A)! Será preciso fazer Recuperação.")
        print("-=" * 50)
