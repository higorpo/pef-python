from prettytable import PrettyTable


class Funcoes:
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

    def serie_perpetua_dado_parcela(A, i):
        valor_presente = A * (1 / i)
        return valor_presente

    def serie_perpetua_dado_presente(P, i):
        valor_parcela = P * i
        return valor_parcela

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

    def grad_geo_achar_presente(A, i, g, n):
        if g != i:
            parte_cima = 1 - (((1 + g) / (1 + i))**n)
            parte_baixo = i - g
            parte_equacao = parte_cima / parte_baixo
        else:
            parte_equacao = n / (1 + i)

        valor_presente = A * parte_equacao
        return valor_presente

    def VPL(tma, cashflows):
        '''
            Valor presente líquido (VPL)
            tma: Taxa de juros
            cashflows: Fluxo de caixa ex.: [-200, 55, 23]
        '''
        total = 0.0
        for i, cashflow in enumerate(cashflows):
            total += cashflow / (1 + tma) ** i
        return total

    def TIR(cashflows, iteracoes=100):
        '''
        Retorna o TIR de um fluxo de caixa

        cashflows: Fluxo de caixa ex.: [-2000, 300, 200, 150]

        >>> TIR([-200.0, 60.0, 60.0, 70.0, 90.0])
        '''
        taxa = 1.0
        investimento = cashflows[0]

        for i in range(1, iteracoes + 1):
            taxa *= (1 - Funcoes.VPL(taxa, cashflows) / investimento)

        return taxa

    def VAUE(taxa, cashflows):
        return Funcoes.seq_uniforme_dado_presente(Funcoes.VPL(taxa, cashflows), taxa, len(cashflows) - 1)

    def payback(taxa, cashflows):
        '''
        Retorna o payback de um investimento

        taxa: Taxa de juros

        cashflows: Fluxo de caixa ex.: [-2000, 300, 200, 150]

        >>> payback(0.20, [-200.0, 60.0, 60.0, 70.0, 90.0])
        '''
        def payback_of_investment(investment, cashflows):
            total, years, cumulative = 0.0, 0, []
            if not cashflows or (sum(cashflows) < investment):
                raise Exception("insufficient cashflows")
            for cashflow in cashflows:
                total += cashflow
                if total < investment:
                    years += 1
                cumulative.append(total)
            A = years
            B = investment - cumulative[years-1]
            C = cumulative[years] - cumulative[years-1]
            return A + (B/C)

        investment, cashflows = cashflows[0], cashflows[1:]
        if investment < 0:
            investment = -investment

        for i, cashflow in enumerate(cashflows):
            cashflows[i] = Funcoes.pagamento_unico_dado_futuro(
                cashflow, taxa, i + 1)

        return payback_of_investment(investment, cashflows)

    def criar_tabela_price(emprestimo, juros, prestacoes):
        '''
            ----
            Cria a tabela de amortização PRICE

            emprestimo: valor do empréstimo

            juros: taxa de juros (ex.: 0.20 = 20%)

            prestacoes: número de prestações
        '''
        saldo_dev = emprestimo
        prestacao = Funcoes.seq_uniforme_dado_presente(
            emprestimo, juros, prestacoes)
        amortizacao = 0
        periodo = 0
        valor_pago_total = prestacao * prestacoes

        t = PrettyTable(['Período', 'Prestação', 'Juros',
                         'Amortização', 'Saldo Dev.'])
        t.add_row([periodo, '-', '-', '-', saldo_dev])

        while periodo < prestacoes:
            periodo += 1
            val_juros = juros * saldo_dev
            amortizacao = prestacao - val_juros
            saldo_dev -= amortizacao

            t.add_row([periodo, round(prestacao, 2), round(val_juros, 2),
                       round(amortizacao, 2), round(saldo_dev, 2)])

        print(t)

        print('valor pago no total: ', round(valor_pago_total, 2))

    def criar_tabela_sac(emprestimo, juros, prestacoes):
        '''
            ----
            Cria a tabela de amortização SAC

            emprestimo: valor do empréstimo

            juros: taxa de juros (ex.: 0.20 = 20%)

            prestacoes: número de prestações
        '''

        saldo_dev = emprestimo
        prestacao = 0
        amortizacao = emprestimo / prestacoes
        periodo = 0
        valor_pago_total = 0

        t = PrettyTable(['Período', 'Prestação', 'Juros',
                         'Amortização', 'Saldo Dev.'])
        t.add_row([periodo, '-', '-', '-', saldo_dev])

        while periodo < prestacoes:
            periodo += 1
            val_juros = juros * saldo_dev
            prestacao = val_juros + amortizacao
            saldo_dev -= amortizacao
            valor_pago_total += prestacao

            t.add_row([periodo, round(prestacao, 2), round(val_juros, 2),
                       round(amortizacao, 2), round(saldo_dev, 2)])

        print(t)

        print('valor pago no total: ', round(valor_pago_total, 2))
