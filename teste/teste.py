# Definindo os parâmetros para os cálculos
# Valores conhecidos
aporte_mensal = 2000  # valor do depósito mensal
aporte_dezembro = 2000  # valor do depósito de 13º salário
taxa_juros_tesouro = 0.13 / 12  # taxa de juros mensal para o Tesouro Selic (13% ao ano)
taxa_juros_cdb = 0.135 / 12  # taxa de juros mensal para CDB (13,5% ao ano)
taxa_juros_poupanca = 0.0875 / 12  # taxa de juros mensal para a poupança (8,75% ao ano)
meses_1_ano = 12  # 1 ano
meses_2_anos = 24  # 2 anos

# Função para calcular o valor final de um investimento com aportes mensais e depósito adicional em dezembro
def calcular_investimento(taxa_juros, meses, aporte_mensal, aporte_dezembro):
    valor_final = 0
    for mes in range(1, meses + 1):
        valor_final = valor_final * (1 + taxa_juros) + aporte_mensal  # juros compostos para o depósito mensal
        if mes == 12:  # adicionado o 13º no mês de dezembro
            valor_final += aporte_dezembro
    return valor_final

# Calculando para 1 ano e 2 anos
valor_tesouro_1_ano = calcular_investimento(taxa_juros_tesouro, meses_1_ano, aporte_mensal, aporte_dezembro)
valor_cdb_1_ano = calcular_investimento(taxa_juros_cdb, meses_1_ano, aporte_mensal, aporte_dezembro)
valor_poupanca_1_ano = calcular_investimento(taxa_juros_poupanca, meses_1_ano, aporte_mensal, aporte_dezembro)

valor_tesouro_2_anos = calcular_investimento(taxa_juros_tesouro, meses_2_anos, aporte_mensal, aporte_dezembro)
valor_cdb_2_anos = calcular_investimento(taxa_juros_cdb, meses_2_anos, aporte_mensal, aporte_dezembro)
valor_poupanca_2_anos = calcular_investimento(taxa_juros_poupanca, meses_2_anos, aporte_mensal, aporte_dezembro)

print(f"Tesouro Selic (1 ano): R${valor_tesouro_1_ano:.2f}")
print(f"CDB (1 ano): R${valor_cdb_1_ano:.2f}")
print(f"Poupança (1 ano): R${valor_poupanca_1_ano:.2f}")
print(f"Tesouro Selic (2 anos): R${valor_tesouro_2_anos:.2f}")
print(f"CDB (2 anos): R${valor_cdb_2_anos:.2f}")
print(f"Poupança (2 anos): R${valor_poupanca_2_anos:.2f}")
