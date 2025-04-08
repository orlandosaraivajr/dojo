''' 

Fonte: https://leetcode.com/problems/integer-to-roman/description/ 

1) Orlando
2)Thiago Barros
3)Guilherme
4)Pedro Rufino
5)Pedro Otavio
6)Thiago dos Santos (Trombose)
7)
8)
9)
10)
'''

values = {}
values[1] = 'I'
values[5] = 'V'
values[10] = 'X'
values[50] = 'L'
values[100] = 'C'
values[500] = 'D'
values[1000] = 'M'

def roman(number):
    retono_romano = ""
    termo = number//50
    if termo == 1:
        retorno_romano = values[50]
        number = number - 50
    termo = number // 5
    if termo == 1:
        retorno_romando = retorno_romando + values[5]
        
    
    pass

assert roman(58) == "LVIII"