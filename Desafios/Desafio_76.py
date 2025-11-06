produtos = ("Camisa", 50, "Tênis", 400, "Bermuda", 80, 
            "Meia", 10, "Casaco", 200, "Cinto", 30)
nome = "Loja DEV"
print("-=" * 30)
print(f"{nome.center(55)}")
print("-=" * 30)
for i in range(0, len(produtos), 2):
    nome = produtos[i]
    preco = produtos[i+1]
    print(f"{nome:.<30}R${preco:>7.2f}")
print("-=" * 30)