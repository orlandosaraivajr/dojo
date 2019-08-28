def sequencia(matriz):
    tamanho = len(matriz)
    for linha in matriz:
        if len(linha) != tamanho:
            return None

    max = 1
    for x in matriz[0]:
        max = max * x

    max2 = 1
    # Linhas
    for i in range(1,  tamanho):
        max2 = 1
        for j in range(tamanho):
            max2 = max2 * matriz[i][j]

        if max2 > max:
            max = max2

    # Colunas
    for i in range(tamanho):
        max2 = 1
        for j in range(tamanho):
            max2 = max2 * matriz[j][i]

        if max2 > max:
            max = max2

    # Diagonais
    max2 = 1
    for i in range(tamanho):
        max2 = max2 * matriz[i][i]

    if max2 > max:
        max = max2

    return max


assert(32 == sequencia([[2, 1, 1, 1, 1],
                       [1, 2, 1, 1, 1], [1, 1, 2, 1, 1],
                       [1, 1, 1, 2, 1], [1, 1, 1, 1, 2]]))
assert(16 == sequencia([[1, 1, 1, 1, 1], [1, 2, 1, 1, 1],
                       [1, 1, 2, 1, 1], [1, 1, 1, 2, 1],
                       [1, 1, 1, 1, 2]]))
assert(None is sequencia([[2, 1, 1, 1, 1], [1, 2, 1, 1, 1],
                         [1, 1, 2, 1, 1], [1, 1, 1, 2, 1],
                         [1, 1, 1, 2]]))
assert(32 == sequencia([[2, 1, 1, 1, 1], [2, 2, 1, 1, 1],
                        [2, 1, 2, 1, 1], [2, 1, 1, 2, 1],
                        [2, 1, 1, 1, 2]]))
assert(32 == sequencia([[2, 2, 2, 2, 2], [1, 1, 1, 1, 1],
                        [1, 1, 2, 1, 1], [1, 1, 1, 2, 1],
                        [1, 1, 1, 1, 2]]))
