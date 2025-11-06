r1 = float(input("Digite o valor do primeiro lado: "))
r2 = float(input("Digite o valor do segundo lado: "))
r3 = float(input("Digite o valor do terceiro lado: "))
if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print("Essas retas formam um triângulo ", end = "")
    if r1 == r2 == r3:
        print("Equilátero.")
    elif r1 != r2 != r3 != r1:
        print("Escaleno.")
    else:
        print("Isósceles.")
else:
    print("Essas retas não formam um triângulo.")
