from combinacao_fatores_1 import *

# === Série uniformes deslocadas
# Para achar o valor presented de uma série uniforme deslocada, primeiro se encontra o valor no tempo em que a série
# começa, utilizando a fórmula (P/A, i, n), com n sendo igual ao número de períodos entre o final da série e o "começo"
# dela. Após isso, esse valor futuro encontrado é levado para o presente, através da fórmula (P/F, i, n).

# valor(P/A, i n')(P/F, i n")

# Para se achar o valor futuro de uma série uniforme deslocada, é mais fácil ainda. Basta utilizar a fórmula
# (F/A, i, n), com n sendo igual ao período entre o começo das parceças e o fim delas.

# Exemplo do slide
# print(pagamento_unico_dado_futuro(
# seq_uniforme_dado_parcela(500, 0.08, 6), 0.08, 2) + 5000)

# print(seq_uniforme_dado_presente(pagamento_unico_dado_futuro(
#    seq_uniforme_dado_parcela(8000, 0.16, 6), 0.16, 2), 0.16, 8))

# === Quantias aleatórias em séries uniformes
# A série uniforme é tratada como uma série uniforme comum, precisando fazer o deslocamento caso elas esteja deslocada,
# e os fluxos de caixa aleatórios são tratados com as fórmulas de pagamento único.

# === Cálculos de gradientes deslocados
# Primeiro se calcula o gradiente na posição em que ele está, lembrando que o valor presente de um gradiente aritmético
# sempre estará localizado dois períodos antes do gradiente iniciar, por meio da fórmula (P/G, i, n), em que o n é o
# número de períodos após o começo do gradiente. Então, é utilizada a fórmula de valor único (P/F, i, n), para levar o
# valor para o presente e obter o resultado final.

# Quando se há tanto uma série A como uma série G no mesmo problema, ambas são resolvidas, então somadas (pois
# provavelmente estarão iniciando no mesmo período), e o resultado final é levado par o presente.

# Exemplo do slide
# exemplo_resposta = seq_uniforme_dado_parcela(
# 100, 0.07, 8) + pagamento_unico_dado_futuro(gradiente_aritmetico_achar_presente(50, 0.07, 5), 0.07, 3)
# print(exemplo_resposta)

# === Gradientes aritméticos deslocados decrescentes
# Primeiro se completa os valores faltantes da série G para montar uma série uniforme A. Então, a série uniforme é
# calculada. Após isso, é calculado a série gradiente G artificial, ela é trazida para o presente, e por fim subtraída
# do valor presente da série uniforme A, resultando no valor presente original.

# === Fatores de gradiente geométrico
# Além dos símbolos i e n, iremos também utilizar o termo g, que é a taxa de variação constante pela qual os montantes
# se elevam ou decrescem de um período para o seguinte.


def grad_geo_achar_presente(A, i, g, n):
    if g != i:
        parte_cima = 1 - (((1 + g) / (1 + i))**n)
        parte_baixo = i - g
        parte_equacao = parte_cima / parte_baixo
    else:
        parte_equacao = n / (1 + i)

    valor_presente = A * parte_equacao
    return valor_presente

# Exemplo do slide
    # exemplo_resposta_3 = pagamento_unico_dado_futuro(1300, 0.08, 6) - (grad_geo_achar_presente(
    # 1700, 0.08, 0.11, 6) + 8000)
    # print(exemplo_resposta_3)
