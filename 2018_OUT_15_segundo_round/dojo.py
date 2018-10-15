def fizzbuzz(numero):
    if type(numero) is not int:
        return None

    if numero % 15 == 0:
        return 'FizzBuzz'
    elif numero % 3 == 0:
        return 'Fizz'
    elif numero % 5 == 0:
        return 'Buzz'
    else:
        return numero


assert(fizzbuzz(3) == 'Fizz')
assert(fizzbuzz(6) == 'Fizz')
assert(fizzbuzz(9) == 'Fizz')
assert(fizzbuzz(1) == 1)
assert(fizzbuzz(2) == 2)
assert(fizzbuzz(5) == 'Buzz')
assert(fizzbuzz(15) == 'FizzBuzz')
assert(fizzbuzz('1') is None)
assert(fizzbuzz([1]) is None)
