from combinacao_fatores_1 import *

# 1) CERTO!
principal = 100000
n_periodos = 30
taxa_juros = 0.03
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
first_n_periodos = 10
first_taxa_juros = 0.09
first_prestacao_price = seq_uniforme_dado_presente(
    principal, first_taxa_juros, first_n_periodos)
print(f"\nPrestação Price (antes): {first_prestacao_price}")
saldo_devedor_k = seq_uniforme_dado_parcela(
    first_prestacao_price, 0.09, first_n_periodos - 4)
print(f"Saldo devedor depois do 3º pagamento: {saldo_devedor_k}")

sec_n_periodos = 12
sec_taxa_juros = 0.1
sec_prestacao_price = seq_uniforme_dado_presente(
    saldo_devedor_k, sec_taxa_juros, sec_n_periodos)
print(f"Prestação Price (depois): {sec_prestacao_price}\n")

# 3) Achada na internet
