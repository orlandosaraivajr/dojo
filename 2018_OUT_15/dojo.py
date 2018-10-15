def abnt(nome):
	nomes = nome.split(" ")
	sobr = ['JUNIOR', 'FILHO', 'FILHA', 'NETO', 'NETA']
	dos = ['do']

	tam = len(nomes)

	result = nomes[-1].upper()
	if result in sobr :
		result = nomes[-2].upper() + " " + result
		tam -= 1
	result += ","

	for x in range(tam - 1):
		result += " "
		if 
		result += nomes[x].capitalize()
		
	print(result)
	

	return result

assert(abnt('Orlando Saraiva') == 'SARAIVA, Orlando')
assert(abnt('pedro Pimentel') == 'PIMENTEL, Pedro')
assert(abnt('pedro Pagearo pimentel') == 'PIMENTEL, Pedro Pagearo')
assert(abnt('Orlando Saraiva Junior') == 'SARAIVA JUNIOR, Orlando')
assert(abnt('Orlando Saraiva do Nascimento Junior') == 'NASCIMENTO JUNIOR, Orlando Saraiva do')