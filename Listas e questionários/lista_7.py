from combinacao_fatores_1 import *
import math

# 1) CERTO!
dispendio_1 = pagamento_unico_dado_futuro(9000, 0.1, 2)
dispendio_2 = pagamento_unico_dado_futuro(8000, 0.1, 3)
dispendio_3 = pagamento_unico_dado_futuro(5000, 0.1, 5)
valor_presente_dispendios = dispendio_1 + dispendio_2 + dispendio_3
print(valor_presente_dispendios)

# 2) CERTO!
resposta_2 = pagamento_unico_dado_presente(65000, 0.04, 5)
print(resposta_2)

# 3) CERTO!
resposta_3 = seq_uniforme_dado_presente(1800000, 0.12, 6)
print(resposta_3)

# 4) CERTO!!
resposta_4 = seq_uniforme_dado_presente(3400000, 0.2, 8)
print(resposta_4)

# 5) CERTO!
resposta_5 = seq_uniforme_dado_parcela(190000, 0.1, 5)
print(resposta_5)

# 6) CERTO!
resposta_6 = seq_uniforme_dado_parcela(
    150000, 0.15, 8) + gradiente_aritmetico_achar_presente(10000, 0.15, 8)
print(resposta_6)

# 7)
resposta_7 = math.log(3, 1.1)
print(resposta_7)

# 8) CERTO!


def pagamento_unico_achar_taxa(P, F, n):
    taxa = ((F / P)**(1/n) - 1) * 100
    return taxa


resposta_8 = pagamento_unico_achar_taxa(600000, 1000000, 5)
print(resposta_8)

# 9)
