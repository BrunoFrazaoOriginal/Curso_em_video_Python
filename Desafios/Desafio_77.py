tupla = ("Estudar", "Aprender", "Conhecimento", "Livro", "Aulas", "Professor", "Saber", "Caderno", "Caneta")
for vogal in tupla:
    print(f"\nNa palavra {vogal.upper()} temos as vogais: ", end= " ")
    for letra in vogal:
        if letra.lower() in "aeiou":
            print(letra, end=" ")
print("Fim do programa.")
    