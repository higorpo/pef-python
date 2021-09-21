from prettytable import PrettyTable
from combinacao_fatores_1 import *


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
    taxa = 1.0
    investimento = cashflows[0]

    for i in range(1, iteracoes + 1):
        taxa *= (1 - VPL(taxa, cashflows) / investimento)

    return taxa


def VAUE(taxa, cashflows):
    return seq_uniforme_dado_presente(VPL(taxa, cashflows), taxa, len(cashflows) - 1)


print(VAUE(0.12, [-800000, -60000, -60000, -60000, -60000, -60000, 190000]))


def payback_of_investment(investment, cashflows):
    """The payback period refers to the length of time required 
       for an investment to have its initial cost recovered.

       >>> payback_of_investment(200.0, [60.0, 60.0, 70.0, 90.0])
       3.1111111111111112
    """
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


def payback(taxa, cashflows):
    """The payback period refers to the length of time required
       for an investment to have its initial cost recovered.

       (This version accepts a list of cashflows)

       >>> payback(0.20, [-200.0, 60.0, 60.0, 70.0, 90.0])
       3.1111111111111112
    """
    investment, cashflows = cashflows[0], cashflows[1:]
    if investment < 0:
        investment = -investment

    for i, cashflow in enumerate(cashflows):
        cashflows[i] = pagamento_unico_dado_futuro(cashflow, taxa, i + 1)

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
    prestacao = seq_uniforme_dado_presente(emprestimo, juros, prestacoes)
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
