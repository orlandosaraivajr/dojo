numRomano = {
    'I':1, 
    'V':5, 
    'X':10, 
    'L':50, 
    'C':100, 
    'D':500,
    'M':1000
}


def romanos2int(numero_romano):
    if type(numero_romano) is str:
        valores = []
        for caracter in numero_romano:
            if caracter in 'IVXLCDM':
                valores.append(numRomano[caracter])
            else:
                return None

        ultimo = 0
        vezes = 0
        numero_decimal = 0
        aux = False

        for n in valores[::-1]:
            if n < ultimo and aux is False:
                aux = True
                if n == 1 and (ultimo == 10 or ultimo == 5):
                    numero_decimal -= n
                elif n == 10 and (ultimo == 50 or ultimo == 100):
                    numero_decimal -= n
                elif n == 100 and (ultimo == 500 or ultimo == 1000):
                    numero_decimal -= n
                else: 
                    return None
            else:
                if aux:
                    return None
                numero_decimal += n
                aux = False

            if n == ultimo:
                vezes += 1
            else:
                vezes = 1

            if vezes > 3:
                return None

            ultimo = n
            
        return numero_decimal



assert(romanos2int('III') == 3)
assert(romanos2int('WWW') is None)
assert(romanos2int('XXX') == 30)
assert(romanos2int('XXXX') is None)
assert(romanos2int('IIIII') is None)
assert(romanos2int('IIX') is None)
assert(romanos2int(11) is None)
assert(romanos2int('IXVIII') is None)
assert(romanos2int('XV') == 15)
assert(romanos2int('XXXIX') == 39)
assert(romanos2int('L') == 50)