from time import sleep
brasileirão = ("Palmeiras", "Flamengo", "Cruzeiro", "Botafogo", 
               "Bahia", "Mirassol", "Fluminense", "São Paulo", 
               "Bragantino", "Ceará", "Vasco", "Corinthians", 
               "Grêmio", "Internacional", "Atlético-MG", "Santos", 
               "Vitória", "Fortaleza", "Juventude", "Sport")
print("==" * 30)
print(f"Os cinco primeiros colocados no momento, são: {brasileirão[:5]}")
print("==" * 30)
sleep(2)
print(f"Os times na zona de rebaixamento no momento, são: {brasileirão[-4:]}")
print("==" * 30)
sleep(2)
print("Os times do Brasileirão em ordem alfabética, ficam assim:")
print(sorted(brasileirão))
print("==" * 30)
sleep(2)
print("O time do Botafogo, está na posição: ") 
print(brasileirão.index("Botafogo")+1)
print("==" * 30)
print("Fim do campeonato")