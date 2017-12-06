def buzzfizz(numero):
        if numero % 3 == 0 and numero % 5 == 0:
            return 'fizzbuzz'
        if numero % 3 == 0:
            return 'fizz'
        if numero % 5 == 0:
            return 'buzz'
        return numero


def vetor(inicio, fim):
    # preenchimento da lista de valores
    lista = []
    for x in range(inicio, fim+1):
        lista.append(buzzfizz(x))
    # exibição dos valores com índice
    for indice, conteudo in enumerate(lista):
        print(indice+1, conteudo)


assert(buzzfizz(1) == 1)
assert(buzzfizz(3) == 'fizz')
assert(buzzfizz(5) == 'buzz')
assert(buzzfizz(6) == 'fizz')
assert(buzzfizz(7) == 7)
assert(buzzfizz(10) == 'buzz')
assert(buzzfizz(15) == 'fizzbuzz')

vetor(1, 100)
