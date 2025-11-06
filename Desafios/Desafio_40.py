nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
média = (nota1 + nota2) / 2

if média < 5.0:
    print("Com {} na primeira prova e {} na segunda prova, você ficou com média {} e foi reprovado(a)! Se dedique mais aos estudos!".format(nota1, nota2, média))
elif 5.0 <= média <= 6.9:
    print("Com {} na primeira prova e {} na segunda prova, você ficou com média {} e ficou de recuperação!".format(nota1, nota2, média))
elif média >= 7.0:
    print("Parabéns! Com {} na primeira prova e {} na segunda prova, você ficou com média {} e foi aprovado(a)".format(nota1, nota2, média))
