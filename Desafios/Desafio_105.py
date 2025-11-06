def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    parametro n: Uma ou mais notas de alunos (aceita várias)
    parametro sit: valor opcional, indicando se deve ou não adicionar a situação
    return: dicionário com várias informações sobre a situação da turma.
    """
    r = {}
    r["total"] = len(n)
    r["maior"] = max(n)
    r["menor"] = min(n)
    r["media"] = sum(n) / len(n)
    if sit:
        if r["media"] >= 7:
            r["situação"] = "Boa"
        elif r["media"] >= 5:
            r["situação"] = "Razoável"
        else:
            r["situação"] = "Ruim"
    return r


resp = notas(5.5, 9, 10, sit=True)
print(resp)
#help(notas)