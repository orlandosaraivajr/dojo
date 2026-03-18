dict_romano_decimal = {
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000,
}

def romano_para_decimal(numero_romano):
    soma = 0

    #for caracter in numero_romano:
    #   soma = soma + dict_romano_decimal.get(caracter)
    #return soma

    for i, c in enumerate(numero_romano):
        caractere = dict_romano_decimal[c]
        proximo = dict_romano_decimal[numero_romano[i+1]] if i+1 < len(numero_romano) else 0
        soma += -caractere if caractere < proximo else caractere
    return soma

assert romano_para_decimal('I') == 1
assert romano_para_decimal('IV') == 4
assert romano_para_decimal('V') == 5
assert romano_para_decimal('X') == 10
assert romano_para_decimal('L') == 50
assert romano_para_decimal('C') == 100
assert romano_para_decimal('D') == 500
assert romano_para_decimal('M') == 1000
# Novos números
assert romano_para_decimal('III') == 3
assert romano_para_decimal('XXX') == 30
assert romano_para_decimal('CCC') == 300
assert romano_para_decimal('MMM') == 3000
# Novos testes
assert romano_para_decimal('VIII') == 8
assert romano_para_decimal('LXII') == 62
assert romano_para_decimal('CLVIII') == 158
assert romano_para_decimal('MCXX') == 1120
# Novos testes
assert romano_para_decimal('IV') == 4
assert romano_para_decimal('IX') == 9
assert romano_para_decimal('XC') == 90
# Outros testes da galera
assert romano_para_decimal('XCIX') == 99
assert romano_para_decimal('VII') == 7