'''
Dado um array nums de inteiros distintos, retorne todas as permutações possíveis. 
Você pode retornar a resposta em qualquer ordem.

 
Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]

1) Orlando
2)Guilherme
3)Pedro Otavio
4) Thiago
5) 

Pontos Positivos
================
- Buscamos a documentação ( itertools )
- Terminamos ;)
- Revisitar o conceito de tipagem na função
- Pensamos diversas estratégias.
- Fizemos orientado a testes. Ajustando quando necessário.

Pontos de Melhorias
==================
- Ajustes no retorno da função

'''

import itertools

def permutations(permutation_list) ->list:
    queijo =[]
    # for permutation in itertools.permutations(permutation_list):
    #     queijo.append(permutation)     
    # return queijo
    #return list(itertools.permutations(permutation_list))
    return [p for p in itertools.permutations(permutation_list)]

assert permutations([1,2,3]) == [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
assert permutations([0,1]) == [(0,1),(1,0)]
assert permutations([1]) == [(1,)]