def fizzbuzz(numero):
    if numero == 0:
        return 0
    if numero % 15 == 0:
        return 'fizzbuzz'
    if numero % 5 == 0:
        return 'buzz'
    if numero % 3 == 0:
        return 'fizz'
    else:
        return numero


for i in range(0, 100):
    r = fizzbuzz(i)
    print(r)


assert fizzbuzz(0) == 0
assert fizzbuzz(1) == 1
assert fizzbuzz(2) == 2
assert fizzbuzz(6) == 'fizz'
assert fizzbuzz(3) == 'fizz'
assert fizzbuzz(5) == 'buzz'
assert fizzbuzz(15) == 'fizzbuzz'
assert fizzbuzz(30) == 'fizzbuzz'
