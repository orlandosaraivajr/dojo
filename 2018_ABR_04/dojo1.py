def menor_elemento(lista_parametro):
    '''
    try:
        return sorted(lista_parametro)[0]
    except:
        return None
    '''
    '''
    # metodo 1
    try:
        lista_parametro = list(lista_parametro)
        menor = lista_parametro[0]
        for x in lista_parametro:
                if x < menor:
                    menor = x
    except:
        return None
    return menor
    '''

    # metodo 2
    try:
        return min(lista_parametro)
    except:
        return None


assert(menor_elemento([1, 2, 3, -2]) == -2)
assert(menor_elemento([3, 4, 5, 1, 8]) == 1)
assert(menor_elemento((3, 4, 5, 1, 8)) == 1)
assert(menor_elemento([3, 4, 5, 1, 8, -2, 'oi mundo']) is None)
assert(menor_elemento(['be', 'ab', 'ce', 'ba']) == 'ab')
assert(menor_elemento([]) is None)
assert(menor_elemento({1, 2, 3, 4}) == 1)
assert(menor_elemento([[3], [3, 2, 1], [], [1, 8]]) == [])
assert(menor_elemento([[3, 1], [3, 2, 1], [3], [3, 1, 8, 6]]) == [3])
assert(menor_elemento([[3, 1], [3, 2, 1], [3], [-1, 1, 8, 6]]) ==
       [-1, 1, 8, 6])
