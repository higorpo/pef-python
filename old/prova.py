from combinacao_fatores_1 import *
from combinacao_fatores_2 import *

# 1)
#resposta_1 = pagamento_unico_dado_presente(4371, 0.18, 7)
# print(resposta_1)

# 2)
# Resposta: 12.90179

# 3)
#a = seq_uniforme_dado_parcela(1500, 0.06, 10)
#b = gradiente_aritmetico_achar_presente(500, 0.06, 10)
#resposta = pagamento_unico_dado_presente(1000 + a + b, 0.06, 10)
# print(resposta)
# 1000(F/P; 6%; 10)+1500(P/A; 6%; 10)(F/P; 6%; 10)+500(P/G; 6%; 10)(F/P; 6%; 10)

# 4)
a = pagamento_unico_dado_futuro(8000, 0.09, 2)
b = seq_uniforme_dado_parcela(2000, 0.09, 5)
b_presente = pagamento_unico_dado_futuro(b, 0.09, 4)
vp = 5000 + a + b_presente
resposta_4 = pagamento_unico_dado_presente(vp, 0.09, 10)
print(resposta_4)
# 5000(F/P;9%;10)+8000(P/F;9%;2)(F/P;9%;10)+2000(P/A;9%;5)(P/F;9%;4)(F/P;9%;10)

# 5)
a = seq_uniforme_dado_parcela(15, 0.11, 4)
resposta_5 = 15 + a
print(resposta_5)
a_vista = 75*0.84
print(f'A vista: {a_vista}')
print(f'Diferença: {resposta_5 - a_vista}')

# 6)
vp_deslocado = pagamento_unico_dado_presente(15000, 0.08, 1)
resposta_1 = seq_uniforme_dado_presente(vp_deslocado, 0.08, 6)
print(resposta_1)
# 15000(F/P;8%;1)(A/P;8%;8)

# 7)
resposta_5 = 2000 + seq_uniforme_dado_parcela(
    1800, 0.11, 5) - gradiente_aritmetico_achar_presente(200, 0.11, 5)
print(f'Ultima resposta: {resposta_5}')

# 2000+1800(P/A;11%;5)-200(P/G:11%;5)

# Questão 4 Luiza
a = pagamento_unico_dado_futuro(7000, 0.06, 2)
b = seq_uniforme_dado_parcela(3000, 0.06, 5)
b_presente = pagamento_unico_dado_futuro(b, 0.06, 4)
vp = 5000 + a + b_presente
resposta_4 = pagamento_unico_dado_presente(vp, 0.06, 10)
print(resposta_4)
# 5000(F/P;6%;10)+7000(P/F;6%;2)(F/P;6%;10)+3000(P/A;6%;5)(P/F;6%;4)(F/P;6%;10)
