km = float(input("O carro percorreu quantos quilômetros? "))
dias = int(input("Quantos dias o carro ficou alugado? "))
p = (km * 0.15) + (dias * 60)
print("O carro percorreu {}km, durante {} dias, então o preço a se pagar é de:\nR${:.2f}".format(km, dias, p))
