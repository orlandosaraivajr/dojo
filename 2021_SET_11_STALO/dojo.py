def fizzbuzz(numero):
    if (numero % 3) == 0 and numero % 5 == 0:
        return 'FizzBuzz'
    elif numero % 3 == 0:
        return 'Fizz'
    elif numero % 5 == 0:
        return 'Buzz'
    return numero


for numero in range(101):
    print(fizzbuzz(numero))


assert(fizzbuzz(1) == 1)
assert(fizzbuzz(2) == 2)
assert(fizzbuzz(3) == 'Fizz')
assert(fizzbuzz(4) == 4)
assert(fizzbuzz(5) == 'Buzz')
assert(fizzbuzz(6) == 'Fizz')
assert(fizzbuzz(9) == 'Fizz')
assert(fizzbuzz(10) == 'Buzz')
assert(fizzbuzz(15) == 'FizzBuzz')
