def fizzbuzz (numero):
	if numero%15 == 0 :
		return 'fizzbuzz'
	elif numero%3 == 0 :
		return 'fizz'
	elif numero%5 == 0 :
		return 'buzz'
	else : 
		return numero


assert(fizzbuzz(1) == 1)
assert(fizzbuzz(2) == 2)
assert(fizzbuzz(3) == 'fizz')
assert(fizzbuzz(5) == 'buzz')
assert(fizzbuzz(15) == 'fizzbuzz')