frase = str(input("Digite a sua frase: ")).strip()
print("A letra 'a' aparece {} vezes na frase.".format(frase.lower().count('a')))
print("A primeira letra 'a' apareceu na posição {}.".format(frase.lower().find('a')+1))
print("A última letra 'a' apareceu na posição {}.".format(frase.lower().rfind('a')+1))
