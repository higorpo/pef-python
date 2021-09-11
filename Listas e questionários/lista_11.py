from combinacao_fatores_1 import *

# 1) CERTO!
q1_vida_util = 6
q1_taxa_juros = 0.15

vel_var_custo_aquisicao = 250000
vel_var_custo_operacional_anual = 231000
vel_var_custo_revisao_geral_ano_4 = 140000
vel_var_valor_residual = 50000

vel_var_vpl = - vel_var_custo_aquisicao - \
    seq_uniforme_dado_parcela(vel_var_custo_operacional_anual, q1_taxa_juros, q1_vida_util) - \
    pagamento_unico_dado_futuro(vel_var_custo_revisao_geral_ano_4, q1_taxa_juros, 4) + \
    pagamento_unico_dado_futuro(
        vel_var_valor_residual, q1_taxa_juros, q1_vida_util)

print('--- QUESTÃO 1 ---')
print(vel_var_vpl)

vel_dupla_custo_aquisicao = 224000
vel_dupla_custo_operacional_anual = 235000
vel_dupla_custo_revisao_geral_ano_3 = 26000
vel_dupla_valor_residual = 10000

vel_dupla_vpl = - vel_dupla_custo_aquisicao - \
    seq_uniforme_dado_parcela(vel_dupla_custo_operacional_anual, q1_taxa_juros, q1_vida_util) - \
    pagamento_unico_dado_futuro(vel_dupla_custo_revisao_geral_ano_3, q1_taxa_juros, 3) + \
    pagamento_unico_dado_futuro(
        vel_dupla_valor_residual, q1_taxa_juros, q1_vida_util)

print(vel_dupla_vpl)


# 2) CERTO!
q2_vida_util = 4  # MMC entre 4 e 2
q2_taxa_juros = 0.10

JX_custo_aquisicao = 205000
JX_custo_operacional_anual = 29000
JX_valor_residual = 2000

JX_vpl = - JX_custo_aquisicao - \
    seq_uniforme_dado_parcela(JX_custo_operacional_anual, q2_taxa_juros, q2_vida_util) - \
    pagamento_unico_dado_futuro(JX_custo_aquisicao - JX_valor_residual, q2_taxa_juros, 2) + \
    pagamento_unico_dado_futuro(JX_valor_residual, q2_taxa_juros, q2_vida_util)

print('\n--- QUESTÃO 2 ---')
print(JX_vpl)

KZ_custo_aquisicao = 235000
KZ_custo_operacional_anual = 27000
KZ_valor_residual = 20000

KZ_vpl = - KZ_custo_aquisicao - \
    seq_uniforme_dado_parcela(KZ_custo_operacional_anual, q2_taxa_juros, q2_vida_util) + \
    pagamento_unico_dado_futuro(
        KZ_valor_residual, q2_taxa_juros, q2_vida_util)

print(KZ_vpl)


# 3) CERTO!
taxa_juros_A = 0.0609  # i a.a. = (1 + 0,03)^2 – 1 = 6,09%
# periodos = 12 semestres

valor_contrato_A = 1000000
plano_A = - valor_contrato_A - \
    seq_uniforme_dado_parcela(valor_contrato_A, taxa_juros_A, 5)

print('\n--- QUESTÃO 3 ---')
print(plano_A)

taxa_juros_B = 0.03  # 6%/2
valor_contrato_B = 600000
plano_B = - valor_contrato_B - seq_uniforme_dado_parcela(
    valor_contrato_B, taxa_juros_B, 11)

print(plano_B)

taxa_juros_C = 0.03  # 6%/2
valor_contrato_C = 1500000
valor_outro_C = 500000
plano_C = - valor_contrato_C - \
    pagamento_unico_dado_futuro(valor_outro_C, taxa_juros_C, 4) - \
    pagamento_unico_dado_futuro(valor_contrato_C, taxa_juros_C, 6) - \
    pagamento_unico_dado_futuro(valor_outro_C, taxa_juros_C, 10)

print(plano_C)
