from combinacao_fatores_1 import *


# 1)
q1_TMA = 0.10
q1_periodo = 6

plastica_invest_inicial = 75000
plastica_custo_anual = 27000

# Sem renovação
# plastica_vlp = - plastica_invest_inicial - \
#    seq_uniforme_dado_parcela(plastica_custo_anual, q1_TMA, q1_periodo)

# Com renovação
plastica_vlp = - plastica_invest_inicial - \
    seq_uniforme_dado_parcela(plastica_custo_anual, q1_TMA, q1_periodo) - \
    pagamento_unico_dado_futuro(plastica_invest_inicial, q1_TMA, 2) - \
    pagamento_unico_dado_futuro(plastica_invest_inicial, q1_TMA, 4)

print('\n--- QUESTÃO 1 ---')
print(f"Caixa plástica: {plastica_vlp}")

aluminio_invest_inicial = 125000
aluminio_custo_anual = 12000
aluminio_venda_equip = 30000

# Sem renovação
# aluminio_vlp = - aluminio_invest_inicial - seq_uniforme_dado_parcela(
#    aluminio_custo_anual, q1_TMA, q1_periodo) + pagamento_unico_dado_futuro(aluminio_venda_equip, q1_TMA, 3)

# Com renovação
aluminio_vlp = - aluminio_invest_inicial - seq_uniforme_dado_parcela(
    aluminio_custo_anual, q1_TMA, q1_periodo) - pagamento_unico_dado_futuro(aluminio_invest_inicial - aluminio_venda_equip, q1_TMA, 3) + \
    pagamento_unico_dado_futuro(aluminio_venda_equip, q1_TMA, 6)

print(f"Caixa alumínio: {aluminio_vlp}")

# 2)
q2_TMA = 0.07
projeto_A = -15000 + seq_uniforme_dado_parcela(2800, q2_TMA, 4) + pagamento_unico_dado_futuro(
    seq_uniforme_dado_parcela(3300, q2_TMA, 4), q1_TMA, 4)
projeto_B = -7000 + seq_uniforme_dado_parcela(2000, q2_TMA, 8) + seq_uniforme_dado_parcela(1000, q2_TMA, 2) - pagamento_unico_dado_futuro(
    7000, q2_TMA, 4) + pagamento_unico_dado_futuro(seq_uniforme_dado_parcela(1000, q2_TMA, 2), q2_TMA, 4)
print('\n--- QUESTÃO 2 ---')
print(f"Projeto A: {projeto_A}")
print(f"Projeto B: {projeto_B}")

payback_A = seq_uniforme_dado_parcela(2800, q2_TMA, 4) + pagamento_unico_dado_futuro(
    seq_uniforme_dado_parcela(3300, q2_TMA, 2), q2_TMA, 4)

payback_B = seq_uniforme_dado_parcela(
    3000, q2_TMA, 2) + pagamento_unico_dado_futuro(2000, q2_TMA, 3)
print('\n')
print(f"Payback A: {payback_A}")
print(f"Payback B: {payback_B}")
