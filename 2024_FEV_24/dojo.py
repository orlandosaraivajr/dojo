def fizzbuzz(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return "FizzBuzz"
    if numero % 3 == 0:
        return "Fizz"
    if numero % 5 == 0:
        return "Buzz"
    return numero
    

for number in range(1,101):
    print(fizzbuzz(number))

assert(fizzbuzz(1) == 1)
assert(fizzbuzz(2) == 2)
assert(fizzbuzz(3) == "Fizz")
assert(fizzbuzz(4) == 4)
assert(fizzbuzz(5) == "Buzz")
assert(fizzbuzz(15) == "FizzBuzz")
assert(fizzbuzz(37) == 37)
assert(fizzbuzz(50) == "Buzz")
assert(fizzbuzz(36) == "Fizz")
assert(fizzbuzz(90) == "FizzBuzz")
assert(fizzbuzz(100) == "Buzz")
