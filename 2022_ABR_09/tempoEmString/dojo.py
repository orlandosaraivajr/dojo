def horas(hora, minuto):
    hora_string = ''
    minuto_string = ''
    horas = {
        1: 'uma',
        2: 'duas',
        3: 'três',
        4: 'quatro',
        5: 'cinco',
        6: 'seis',
        7: 'sete',
        8: 'oito',
        9: 'nove',
        10: 'dez',
        11: 'onze',
        12: 'doze',
    }

    minutos = {
        1: 'um',
        2: 'dois',
        3: 'três',
        4: 'quatro',
        5: 'cinco',
        6: 'seis',
        7: 'sete',
        8: 'oito',
        9: 'nove',
        10: 'dez',
        11: 'onze',
        12: 'doze',
        13: 'treze',
        14: 'catorze',
        15: 'quinze',
        16: 'dezesseis',
        17: 'dezessete',
        18: 'dezoito',
        19: 'dezenove',
        20: 'vinte',
        21: 'vinte e um',
        22: 'vinte e dois',
        23: 'vinte e três',
        24: 'vinte e quatro',
        25: 'vinte e cinco',
        26: 'vinte e seis',
        27: 'vinte e sete',
        28: 'vinte e oito',
        29: 'vinte e nove',
        30: 'meia',
    }

    hora_string = horas.get(hora)

    minuto_string = minutos.get(minuto)

    valido = True
    if hora >= 12:
        valido = False
    if minuto >= 60:
        valido = False

    if not valido:  
        return 'hora inválida'

    if minuto < 30:
        resultado = f'{hora_string} hora e {minuto_string} minuto'
    elif minuto == 30:
        resultado = f'{hora_string} hora e {minuto_string}'
    elif minuto > 30:
        minuto = 60 - minuto
        hora = hora + 1
        hora_string = horas.get(hora)
        minuto_string = minutos.get(minuto)
        resultado = f'{minuto_string} para as {hora_string}'
    if not minuto_string:
        resultado = f'{hora_string} horas'

    print(resultado)
    print(hora)
    return resultado


assert(horas(6, 0) == 'seis horas')
assert(horas(5, 1) == 'cinco hora e um minuto')
assert(horas(6, 1) == 'seis hora e um minuto')
assert(horas(6, 20) == 'seis hora e vinte minuto')
assert(horas(6, 21) == 'seis hora e vinte e um minuto')
assert(horas(6, 29) == 'seis hora e vinte e nove minuto')
assert(horas(6, 30) == 'seis hora e meia')
assert(horas(6, 35) == 'vinte e cinco para as sete')
assert(horas(6, 45) == 'quinze para as sete')
assert(horas(18, 68) == 'hora inválida')
assert(horas(6, 68) == 'hora inválida')
assert(horas(12, 35) == 'hora inválida')
assert(horas(-3, 60) == 'hora inválida')
assert(horas(3, 60) == 'hora inválida')
assert(horas(1, 1) == 'uma hora e um minuto')

# manda o deploy will lopes