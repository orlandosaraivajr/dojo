'''
O que foi bom ?
    - Participação de outras turmas
    - Problema fácil para entendimento
    - Ajuda da platéia
    - Entendimento do código
    - Apoio do professor
O que podemos melhorar ?
    - Fazer novos dojos com problemas mais desafiores
    - Poucos participantes
    
'''
def fizzbuzz(numero):
    if numero % 5 == 0 and numero % 3 == 0:
        return 'FizzBuzz'
    elif numero % 3 == 0:
        return 'Fizz'
    elif numero % 5 == 0:
        return 'Buzz'
    return numero

assert fizzbuzz(1) == 1
assert fizzbuzz(2) == 2
assert fizzbuzz(3) == 'Fizz'
assert fizzbuzz(4) == 4
assert fizzbuzz(5) == 'Buzz'
assert fizzbuzz(6) == 'Fizz'
assert fizzbuzz(7) == 7
assert fizzbuzz(8) == 8
assert fizzbuzz(9) == 'Fizz'
assert fizzbuzz(10) == 'Buzz'
assert fizzbuzz(11) == 11
assert fizzbuzz(12) == 'Fizz'
assert fizzbuzz(13) == 13
assert fizzbuzz(14) == 14
assert fizzbuzz(15) == 'FizzBuzz'
assert fizzbuzz(30) == 'FizzBuzz'
assert fizzbuzz(45) == 'FizzBuzz'
assert fizzbuzz(90) == 'FizzBuzz'
assert fizzbuzz(77) == 77   

for i in range(1,101):
    print(fizzbuzz(i))