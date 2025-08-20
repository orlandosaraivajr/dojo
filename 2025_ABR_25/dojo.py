def int_to_roman(numero):
    
    valores = [
    (1000, 'M'),(900, 'CM'),(500, 'D'),(400,'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40,'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1,'I')]

    resultado = ''
    for valor,simbolo in valores:
        while numero >= valor:
            resultado += simbolo
        '''
        - Entrada = n = 1987
        - O primeiro valor em valores  é 1000 ('M)
        - Enquanto 1987 >= 1000, add 'M' no resultado e subtraímos 1000:
        - resultado = 'M', n = 987
        ''' 
            n -= valor
    return resultado           
    
        

assert( int_to_roman(3) == 'III') # 1 + 1 + 1
assert( int_to_roman(58) == 'LVIII') # 50 + 5 + 1 + 1 + 1