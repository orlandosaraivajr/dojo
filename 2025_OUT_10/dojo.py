def fizzbuzz(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return 'Fizz Buzz'
    if numero % 3 == 0:
        return 'Fizz'
    if numero % 5 == 0:
        return 'Buzz'
    return str(numero)

assert fizzbuzz(1) == '1'
assert fizzbuzz(2) == '2'
assert fizzbuzz(3) == 'Fizz'
assert fizzbuzz(6) == 'Fizz'
assert fizzbuzz(5) == 'Buzz'
assert fizzbuzz(10) == 'Buzz'
assert fizzbuzz(15) == 'Fizz Buzz'
assert fizzbuzz(30) == 'Fizz Buzz'
assert fizzbuzz(54) == 'Fizz'
'''
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        "fizzbuzz"
    elif i % 3 == 0:
        "fizz"'''
        
for numero in range(1, 101):
    print(fizzbuzz(numero))