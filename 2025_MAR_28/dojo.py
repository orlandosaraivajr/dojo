def fizzbuzz(numero):
    if (numero % 3 == 0) and (numero % 5 == 0):
         return 'FizzBuzz'
    elif numero % 3 == 0:
        return 'Fizz'
    elif numero % 5 == 0:
        return 'Buzz'
    else:
        return numero


assert fizzbuzz(1) == 1
assert fizzbuzz(2) == 2
assert fizzbuzz(3) == 'Fizz'
assert fizzbuzz(4) == 4
assert fizzbuzz(5) == "Buzz"
assert fizzbuzz(15) == "FizzBuzz"
assert fizzbuzz(30) == "FizzBuzz"
assert fizzbuzz(35) == "Buzz"
assert fizzbuzz(40) == "Buzz"
assert fizzbuzz(11) == 11
assert fizzbuzz(12) == "Fizz"
assert fizzbuzz(45) == "FizzBuzz"
assert fizzbuzz(99) == "Fizz"
assert fizzbuzz(100) == "Buzz"

for i in range(1,101):
    print(fizzbuzz(i))