# === Pagamento único
def pagamento_unico_dado_futuro(F, i, n):
    # (P/F, i, n)
    '''
    Determina o montante P a partir de um único valor futuro F, que foi acumulado depois
    de n períodos.

    P: principal/presente
    F: futuro
    i: taxa (em decimal)
    n: nº de períodos
    '''
    parte_cima = F
    parte_baixo = (1 + i)**n
    valor_presente = parte_cima / parte_baixo
    return valor_presente


def pagamento_unico_dado_presente(P, i, n):
    # (F/P, i, n)
    '''
    Determina o montante F acumulado depois de n períodos a partir de um único
    valor presente P.

    P: principal/presente
    F: futuro
    i: taxa (em decimal)
    n: nº de períodos
    '''
    valor_futuro = P * ((1 + i)**n)
    return valor_futuro


# Exemplos dos slides
    #print(pagamento_unico_dado_presente(50000, 0.2, 5))
    #print(pagamento_unico_dado_futuro(50000, 0.2, 3))


# === Fator de sequência uniforme e rec. de capital (P/A e A/P)

# A forma de encontrar o valor presente de uma série uniforme nada mais é do que
# considerar cada valor A (parcela) como valor F, pegar esses valores futuros, trazê-los
# para o presente um-a-um (usando P/F), e somá-los no final.

# A série uniforme padrão inicia SEMPRE no período 1!

def seq_uniforme_dado_parcela(A, i, n):
    # (P/A, i, n)
    '''
    Determina o valor presente P acumulado dado o valor das parcelas (A)
    em n períodos.

    P: principal/presente
    A: valor das parcelas
    i: taxa (em decimal)
    n: nº de períodos
    '''
    parte_cima = ((1 + i)**n) - 1
    parte_baixo = i * ((1 + i)**n)
    valor_presente = A * (parte_cima/parte_baixo)
    return valor_presente


def seq_uniforme_dado_presente(P, i, n):
    # (A/P, i, n)
    '''
    Determina o valor das parcelas (A, ou seja, o incremento a cada período) dado o
    valor presente (P)

    P: principal/presente
    A: valor das parcelas
    i: taxa (em decimal)
    n: nº de períodos
    '''

    parte_cima = i * ((1 + i)**n)
    parte_baixo = ((1 + i)**n) - 1
    valor_parcela = P * (parte_cima / parte_baixo)
    return valor_parcela

# === Fator amortização e Capitalização sequência uniforme (A/F e F/A)

# O fator de amortização determina a sequeência anual uniforme A que é equivalente
# a determinado valor futuro D. É basicamente a mesma lógia que o fator de sequência
# uniforme, a diferença é que aqui iremos trazer cada valor de parcela A para o futuro,
# e depois somá-los.


def fator_amortizacao_dado_futuro(F, i, n):
    # (A/F, i, n)
    '''
    Determina o valor das parcelas A dado o valor futuro F em n períodos.

    F: valor futuro
    A: valor das parcelas
    i: taxa (em decimal)
    n: nº de períodos
    '''
    parte_cima = i
    parte_baixo = ((1 + i)**n) - 1
    valor_parcela = F * (parte_cima / parte_baixo)
    return valor_parcela


def fator_amortizacao_dado_parcela(A, i, n):
    # (F/A, i, n)
    '''
    Determina o valor futuro F dado o valor das parcelas A em n períodos.

    F: valor futuro
    A: valor das parcelas
    i: taxa (em decimal)
    n: nº de períodos
    '''
    parte_cima = ((1 + i)**n) - 1
    parte_baixo = i
    valor_futuro = A * (parte_cima / parte_baixo)
    return valor_futuro


# Exemplos dos slides
    #print(seq_uniforme_dado_parcela(600, 0.16, 9))
    #print(10 + seq_uniforme_dado_parcela(10, 0.1, 4))


# === Séries perpétuas
# Quando o número de períodos em uma série uniforme é grande, pode-se considerá-la infinita

def serie_perpetua_dado_parcela(A, i):
    valor_presente = A * (1 / i)
    return valor_presente


def serie_perpetua_dado_presente(P, i):
    valor_parcela = P * i
    return valor_parcela

# Exemplo dos slides
    #print(serie_perpetua_dado_parcela(10000, 0.01))


# === Fatores de gradiente aritmético (P/G, F/G, A/G)
# Um gradiente aritmético é uma sequência de fluxo de caixa que cresce ou decresce
# de acordo com um valor constante.

# A série G padrão inicia SEMPRE no período 2!

def gradiente_aritmetico_achar_presente(G, i, n):
    parte_cima_esq = ((1 + i)**n) - 1
    parte_baixo_esq = i * ((1 + i)**n)
    parte_esq = parte_cima_esq / parte_baixo_esq

    parte_cima_dir = n
    parte_baixo_dir = (1 + i)**n
    parte_dir = parte_cima_dir / parte_baixo_dir

    valor_presente = (G / i) * (parte_esq - parte_dir)
    return valor_presente


def gradiente_aritmetico_achar_futuro(G, i, n):
    parte_esq = 1 / i

    parte_cima_dir = ((1 + i)**n) - 1
    parte_baixo_dir = i
    parte_dir = (parte_cima_dir / parte_baixo_dir) - n

    valor_futuro = G * (parte_esq * parte_dir)
    return valor_futuro


def gradiente_aritmetico_achar_parcela(G, i, n):
    parte_esq = 1 / i

    parte_cima_dir = n
    parte_baixo_dir = ((1 + i)**n) - 1
    parte_dir = (parte_cima_dir / parte_baixo_dir)

    valor_parcela = G * (parte_esq - parte_dir)
    return valor_parcela

# Exemplo dos slides
    # print(gradiente_aritmetico_achar_presente(100000, 0.05, 10) +
    #      seq_uniforme_dado_parcela(500000, 0.05, 10))
