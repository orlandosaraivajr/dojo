
'''
Valor mínimo: -2
Valor máximo: 92
Número de elementos na seqüência: 6
Valor médio: 21.83
'''
def estatistica(*args):
    minimo =  sorted(args)[0]
    maximo =  sorted(args)[-1]
    num_elementos = len(args)
    media = round(sum(args) / num_elementos, 2)
    retorno = (minimo, maximo, num_elementos, media)
    return retorno


assert estatistica(6, 9, 15, -2, 92, 11) == (-2, 92, 6, 21.83)
assert estatistica(6, 9, 15, 55, 80, -6) == (-6, 80, 6, 26.5)
assert estatistica(-6) == (-6, -6, 1, -6)
