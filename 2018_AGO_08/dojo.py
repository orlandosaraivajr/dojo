def saque(valor):

    lista = []
    notas = [100, 50, 20, 10]

    for nota in notas:
        quantidade = valor//nota
        lista.append(quantidade)
        valor = valor - (quantidade * nota)

    if valor != 0:
        return None

    return lista

    '''

    quantidade = valor//100
    lista.append(quantidade)
    valor = valor - (quantidade * 100)

    quantidade = valor//50
    lista.append(quantidade)
    valor = valor - (quantidade * 50)

    quantidade = valor//20
    lista.append(quantidade)
    valor = valor - (quantidade * 20)

    quantidade = valor//10
    lista.append(quantidade)
    valor = valor - (quantidade * 10)
    '''


def saque_limitado(valor, disponiveis):

    lista = []
    notas = [100, 50, 20, 10]

    for nota, max_ in zip(notas, disponiveis):
        quantidade = valor//nota
        if quantidade > max_:
            quantidade = max_
        lista.append(quantidade)
        valor = valor - (quantidade * nota)

    if valor != 0:
        return None

    return lista


assert(saque(100) == [1, 0, 0, 0])
assert(saque(120) == [1, 0, 1, 0])
assert(saque(50) == [0, 1, 0, 0])
assert(saque(80) == [0, 1, 1, 1])
assert(saque(340) == [3, 0, 2, 0])
assert(saque(25) is None)

assert(saque_limitado(100, [0, 2, 0, 0]) == [0, 2, 0, 0])
assert(saque_limitado(120, [0, 4, 4, 4]) == [0, 2, 1, 0])
assert(saque_limitado(50, [0, 0, 0, 10]) == [0, 0, 0, 5])
assert(saque_limitado(100, [3, 3, 3, 3]) == [1, 0, 0, 0])
assert(saque_limitado(280, [1, 3, 3, 10]) == [1, 3, 1, 1])
assert(saque_limitado(25, [1, 3, 3, 10]) is None)
