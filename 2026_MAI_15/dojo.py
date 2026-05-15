# função do fizzbuzz
def fizzbuzz(numero):
    if (numero % 3 == 0) and (numero % 5 == 0):
        return 'fizzbuzz'
    elif numero % 3 == 0:
        return 'fizz'
    elif numero % 5 == 0:
        return 'buzz'
    
    else:
        return numero
    

# teste unitario
assert fizzbuzz(1) == 1
assert fizzbuzz(2) == 2
assert fizzbuzz(3) == 'fizz'
assert fizzbuzz(4) == 4
assert fizzbuzz(5) == 'buzz'
assert fizzbuzz(6) == 'fizz'
assert fizzbuzz(7) == 7
assert fizzbuzz(15) == 'fizzbuzz'
assert fizzbuzz(30) == 'fizzbuzz'

for x in range(1, 101):
    print(fizzbuzz(x))