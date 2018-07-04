def multiprica(a, b):
    return a*b


def produto_vetor(vetor_a, vetor_b):
    if len(vetor_a) == len(vetor_b):
        return sum(list(map(multiprica, vetor_a, vetor_b)))


'''
    if len(vetor_a) == len(vetor_b):
        produto = 0
        for x in range(len(vetor_a)):
            produto = produto + vetor_a[x] * vetor_b[x]
        return produto
    return None
'''

assert(produto_vetor([3, 4], [-2, 5]) == 14)
assert(produto_vetor([1, 7], [2, -3]) == -19)
assert(produto_vetor([1, 7, 5], [2, 3]) is None)
assert(produto_vetor([1, 2, 3], [1, 2, 3]) == 14)
assert(produto_vetor([], []) == 0)
assert (multiprica(10, 2) == 20)
