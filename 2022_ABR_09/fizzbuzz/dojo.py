def dojo(numero):
    if numero % 5 == 0 and numero % 3 == 0:
        return 'Fizz Buzz'
    elif numero % 3 == 0:
        return 'Fizz'
    elif numero % 5 == 0:
        return 'Buzz'
    return numero


assert(dojo(1) == 1)
assert(dojo(2) == 2)
assert(dojo(4) == 4)
assert(dojo(3) == 'Fizz')
assert(dojo(5) == 'Buzz')
assert(dojo(9) == 'Fizz')
assert(dojo(15) == 'Fizz Buzz')
assert(dojo(30) == 'Fizz Buzz')
assert(dojo(100) == 'Buzz')

for x in range(1,100):
    print(dojo(x))