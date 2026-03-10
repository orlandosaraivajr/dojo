
def fizzbuzz(numero):
    if numero %3 == 0 and numero %5 == 0:
        
        return 'FizzBuzz'
    elif numero %5 == 0:
        return 'Buzz'
    elif numero%3 ==0:
        return 'Fizz'       
    else:
        return numero

assert fizzbuzz(1) == 1
assert fizzbuzz(3) == 'Fizz'
assert fizzbuzz(5) == 'Buzz'
assert fizzbuzz(6) == 'Fizz'
assert fizzbuzz(9) == 'Fizz'
assert fizzbuzz(10) == 'Buzz'
assert fizzbuzz(15) == 'FizzBuzz'
assert fizzbuzz(20) == 'Buzz'
assert fizzbuzz(2) == 2
assert fizzbuzz(4) == 4
assert fizzbuzz(30) == 'FizzBuzz'
for item in range(1,101): 
    print(fizzbuzz(item))