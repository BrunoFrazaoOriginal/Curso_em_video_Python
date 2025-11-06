def área():
    largura = float(input("Qual a largura do terreno? (m) "))
    comprimento = float(input("Qual o comprimento do terreno? (m) "))
    terreno = largura * comprimento
    print(f"A área do terreno é {terreno:.2f} m².")

área()
