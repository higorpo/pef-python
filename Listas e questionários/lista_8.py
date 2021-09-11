from combinacao_fatores_1 import *
from combinacao_fatores_2 import *


# 1) CERTO!
vp_deslocado = pagamento_unico_dado_presente(20000, 0.08, 1)
resposta_1 = seq_uniforme_dado_presente(vp_deslocado, 0.08, 8)
print(resposta_1)

# 2) CERTO!
II_vp_total = pagamento_unico_dado_futuro(
    seq_uniforme_dado_parcela(10000, 0.1, 15), 0.1, 21)
resposta_2 = seq_uniforme_dado_presente(II_vp_total, 0.1, 2)
print(resposta_2)

# 3) CERTO!
III_seq_1 = seq_uniforme_dado_parcela(1000, 0.15, 3)
III_seq_2 = seq_uniforme_dado_parcela(1000, 0.15, 6)
III_vp = 15000 - (III_seq_1 + III_seq_2 + 2000)
III_valor_x = pagamento_unico_dado_presente(III_vp, 0.15, 7)
print(III_valor_x)

# 4) CERTO!
IV_vp = 40000 - \
    pagamento_unico_dado_futuro(
        seq_uniforme_dado_parcela(2000, 0.1, 3), 0.1, 2)
resposta_4 = seq_uniforme_dado_presente(IV_vp, 0.1, 5)
print(resposta_4)

# 5) CERTO!
resposta_5 = 2000 + seq_uniforme_dado_parcela(
    1800, 0.12, 5) - gradiente_aritmetico_achar_presente(200, 0.12, 5)
print(resposta_5)

# 6) CERTO!
VI_vp = grad_geo_achar_presente(2000, 0.15, 0.1, 7)
resposta_6 = pagamento_unico_dado_presente(VI_vp, 0.15, 7)
print(resposta_6)

# 7) CERTO!
VII_vp = grad_geo_achar_presente(3000, 0.08, 0.05, 4)
resposta_7 = pagamento_unico_dado_presente(VII_vp, 0.08, 4)
print(resposta_7)
