def fizzbuzz(numero:int):
    if type(numero)!=int:
        return 0
    if numero < 0:
        return 0
    if numero == 15:
        return 'Fizzbuzz'
    if numero % 3 == 0:
        return 'Fizz'
    if numero % 5 == 0:
        return 'Buzz'
    return numero

assert fizzbuzz(1) == 1
assert fizzbuzz(2) == 2
assert fizzbuzz(3) == 'Fizz'
assert fizzbuzz(4) == 4
assert fizzbuzz(5) == 'Buzz'
assert fizzbuzz("b") == 0
assert fizzbuzz(6) == 'Fizz'
assert fizzbuzz(7) ==7
assert fizzbuzz(8) ==8
assert fizzbuzz(9) =='Fizz'
assert fizzbuzz(10) =='Buzz'
assert fizzbuzz(11) ==11
assert fizzbuzz(12) =='Fizz'
assert fizzbuzz(13) ==13
assert fizzbuzz(14) ==14
assert fizzbuzz(15) =='Fizzbuzz'
assert fizzbuzz(16) == 16
assert fizzbuzz(17) == 17
assert fizzbuzz(18) == 'Fizz'
assert fizzbuzz(7.5) == 0
assert fizzbuzz('18') == 0
assert fizzbuzz(-1) == 0
assert fizzbuzz(19) == 19
assert fizzbuzz(-3) == 0
assert fizzbuzz(20) == 'Buzz'