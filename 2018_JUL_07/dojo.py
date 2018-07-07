def intervalo(lista):
	lista.sort()
	y = lista[0]
	nova_lista = []
	lista_retorno = []
	#[100, 101, 102, 103, 104, 105, 110, 111, 113, 114, 115,150]
	for x in lista:
		if y + 1 == x:
			nova_lista.append(y)
		else:
			if x - 1 == y:
				nova_lista.append(x) 
			if(nova_lista) != []: 
				lista_retorno.append(nova_lista)
			nova_lista = []
		y = x
		
	print(lista_retorno)
	return lista_retorno

assert(intervalo([100, 101, 102, 103, 104, 105, 110, 111, 113, 114, 115,150]) == [[100-105], [110-111], [113-115], [150]])
assert(intervalo([100, 101, 102, 103, 104, 105]) == [[100-105]])
assert(intervalo([153, 152, 151, 150]) == [[150-153]])