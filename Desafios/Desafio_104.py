def leiaInt(msg):
    while True:
        n = input(msg)
        if n.isdigit():
            n = int(n)
            print(f"Você digitou {n}, que é um número inteiro.")
            return n
        else:
            print("\033[0;31mErro! Digite um número inteiro.\033[m")


n = leiaInt("Digite um número inteiro: ")