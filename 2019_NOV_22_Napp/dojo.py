'''def saque(valor):
notas_100 = 0
notas_50 = 0
notas_20 = 0
notas_10 = 0
if valor >= 100:
    notas_100 = int(valor / 100)
valor -= notas_100 * 100
if valor >= 50:
    notas_50 = int(valor / 50)
valor -= notas_50 * 50
if valor >= 20:
    notas_20 = int(valor / 20)
valor -= notas_20 * 20
if valor >= 10:
    notas_10 = int(valor / 10)
valor -= notas_10 * 10
return valor[notas_100,notas_50,notas_20,notas_10]'''


def withdraw(value):
    cells = [100, 50, 20, 10]
    amount_cells = []
    for cell in cells:
        amount = value // cell
        value -= amount * cell
        amount_cells.append(amount)
    return amount_cells


assert withdraw(30) == [0, 0, 1, 1]
assert withdraw(80) == [0, 1, 1, 1]
assert withdraw(100) == [1, 0, 0, 0]
assert withdraw(110) == [1, 0, 0, 1]
assert withdraw(200) == [2, 0, 0, 0]
assert withdraw(1000000) == [10**4, 0, 0, 0]
