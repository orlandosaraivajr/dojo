
def calculo2(lista):
    menor = min(lista)
    maior = max(lista)
    valores = len(lista)
    media = sum(lista)/valores
    return [menor, maior, valores, round(media, 1)]

assert calculo2([6, 9, 15, -2, 92, 11]) == [-2, 92, 6, 21.8]
assert calculo2([1, 3, 1, 3]) == [1, 3, 4, 2]
