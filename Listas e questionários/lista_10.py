from combinacao_fatores_1 import *

# 1) CERTO!
principal = 100000
n_periodos = 25
taxa_juros = 0.04
prestacao_price = seq_uniforme_dado_presente(principal, taxa_juros, n_periodos)
print(f"Prestação Price: {prestacao_price}")

amortizacao = principal / n_periodos
for k in range(0, n_periodos + 1):
    saldo_devedor = principal - (k * amortizacao)
    juros = taxa_juros * saldo_devedor
    prestacao_sac = amortizacao + juros
    is_greater = prestacao_price > prestacao_sac
    # A prestação só começa 1 período depois pelo visto, por isso o +1
    print(f"Prestação SAC no período {k + 1}: {prestacao_sac}")
    print(is_greater)
    print(f"Saldo devedor {k}: {saldo_devedor}\n")
    if is_greater:
        print(f'Resposta: {k + 1}')
        break

# 2) CERTO!
principal = 500000
first_n_periodos = 8
first_taxa_juros = 0.12
first_prestacao_price = seq_uniforme_dado_presente(
    principal, first_taxa_juros, first_n_periodos)
print(f"\nPrestação Price (antes): {first_prestacao_price}")
saldo_devedor_k = seq_uniforme_dado_parcela(
    first_prestacao_price, 0.12, first_n_periodos - 3)
print(f"Saldo devedor depois do 3º pagamento: {saldo_devedor_k}")

sec_n_periodos = 15
sec_taxa_juros = 0.15
sec_prestacao_price = seq_uniforme_dado_presente(
    saldo_devedor_k, sec_taxa_juros, sec_n_periodos)
print(f"Prestação Price (depois): {sec_prestacao_price}\n")

# 3)
principal = 500000
sac_taxa_juros = 0.05
sac_n_periodos = 12

amortizacao = principal / sac_n_periodos
sac_saldo_devedor_k = principal - (amortizacao * 4)
print(f"Saldo devedor após 4 prestações pagas (SAC): {sac_saldo_devedor_k}")

price_taxa_juros = 0.06
price_n_periodos = 10
price_prestacao = seq_uniforme_dado_presente(
    sac_saldo_devedor_k, price_taxa_juros, price_n_periodos)
print(f"Prestação (Price): {price_prestacao}")

price_saldo_devedor_k = seq_uniforme_dado_parcela(
    price_prestacao, price_taxa_juros, price_n_periodos - 5)
print(f"Saldo devedor depois do 5º pagamento (Price): {price_saldo_devedor_k}")

# for k in range(0, first_n_periodos + 1):
#    saldo_devedor = principal - (k * amortizacao)
#    juros = sac_taxa_juros * saldo_devedor
#    prestacao_sac = amortizacao + juros
#    # A prestação só começa 1 período depois pelo visto, por isso o +1
#    if k == 4:
#        print(f"Prestação SAC no período {k + 1}: {prestacao_sac}")
#        print(f"Saldo devedor {k}: {saldo_devedor}\n")
