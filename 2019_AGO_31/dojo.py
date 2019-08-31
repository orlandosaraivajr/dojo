from functools import reduce

def matrix(matriz):
    maior = 1
    for elem in range(len(matriz)):
    	maior = maior * matriz[elem][elem]

    temp = 1
    for linha in matriz:
    	temp = 1
    	for elem in linha:
    		temp = temp * elem
    	if temp > maior:
        	maior = temp

    return maior


assert(matrix([[2,1,1,1,1],[1,2,1,1,1],[1,1,2,1,1],[1,1,1,2,1],[1,1,1,1,2]]) == 32)
assert(matrix([[2,1,1,1,1],[100,2,1,1,1],[1,1,2,1,1],[1,1,1,2,1],[1,1,1,1,2]]) == 200)
'''
lista = [[2,1,1,1,1],[1,2,1,1,1],[1,1,2,1,1],[1,1,1,2,1],[1,1,1,1,2]]

def soma_linha(x, y):
	return x * y

l = []
for listinha in lista:
	l.append(reduce(lambda x, y: x * y, listinha))

print(l)
'''