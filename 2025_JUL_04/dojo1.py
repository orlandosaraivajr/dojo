# https://leetcode.com/problems/multiply-strings/description/

def soma_listas(lista1, lista2):
    return sorted(lista1 + lista2)


assert soma_listas([],[]) == []
assert soma_listas([],[0]) == [0]
assert soma_listas([1,2,4],[1,3,4]) == [1,1,2,3,4,4]
assert soma_listas([-1,2,4],[1,3,4]) == [-1,1,2,3,4,4]