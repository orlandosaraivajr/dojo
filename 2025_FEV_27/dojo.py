'''
Pontos positivos:
=================
- Problema Desafiador
- Aplicação das estruturas apresentadas em aula
- Participação dos pilotos/copilotos

Pontos de Melhorias:
====================
- Platéia mais unida entorno do problema

'''

dict_dezenas = {
    1: 'dez',
    2: 'vinte',
    3: 'trinta',
    4: 'quarenta',
    5: 'cinquenta',
    6: 'sessenta',
    7: 'setenta',
    8: 'oitenta',
    9: 'noventa',
    10: 'cem'
}

dict_un = {
    1: 'um',
    2: 'dois',
    3: 'tres',
    4: 'quatro',
    5: 'cinco',
    6: 'seis',
    7: 'sete',
    8: 'oito',
    9: 'nove',
    10: 'dez',
    11: 'onze',
    12: 'doze' ,
    13: 'treze' ,
    14: 'quatorze',
    15: 'quinze',
    16: 'dezesseis',
    17: 'dezessete',
    18: 'dezoito',
    19: 'dezenove',
    20: 'vinte',
    30: 'trinta',
    40: 'quarenta',
    50: 'cinquenta'
}

def cheque(valor):
    real, centavos = valor.split('.')
    #valor = ""
    
    int_real = int(real)
    dezena = int_real // 10 * 10
    centena = int_real % 10
    
    if int_real in dict_un:
        print(dict_un[int_real], "reais")
        return dict_un[int_real] + " reais"
    else:
        print(dict_un[dezena], "e", dict_un[centena])
        return dict_un[int_real] + " e " dict_un[centena] + " reais"
    
   
    
    
    
    
    

assert cheque('0.50') == 'cinquenta centavos'
assert cheque('0.40') == 'quarenta centavos'
assert cheque('41.70') == 'quarenta e um reais'
assert cheque('410.70') == 'quarenta e um reais'
# assert cheque('1.50') == 'um real e cinquenta centavos'