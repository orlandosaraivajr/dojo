

def caixa(valor_saque):

    notas_disponiveis = [100, 50, 20, 10]
    valor_a_sacar = valor_saque
    notas_sacadas = [0, 0, 0, 0]
    for key, nota in enumerate(notas_disponiveis):
        valor = valor_a_sacar // nota
        notas_sacadas[key] = valor
        valor_a_sacar -= valor * nota

    return notas_sacadas


assert(caixa(30) == [0, 0, 1, 1])
assert(caixa(80) == [0, 1, 1, 1])
assert(caixa(100) == [1, 0, 0, 0])
assert(caixa(110) == [1, 0, 0, 1])
assert(caixa(300) == [3, 0, 0, 0])
assert(caixa(310) == [3, 0, 0, 1])
assert(caixa(500) == [5, 0, 0, 0])
