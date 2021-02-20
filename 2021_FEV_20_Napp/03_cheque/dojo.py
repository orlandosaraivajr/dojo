def cheque(valor):
    lista_valores = {
        1: "Um",
        2: "Dois",
        3: "Três",
        4: "Quatro",
        5: "Cinco",
        6: "Seis",
        7: "Sete",
        8: "Oito",
        9: "Nove",
        10: "Dez",
        11: "Onze",
        12: "Doze",
        13: "Treze",
        14: "Quatorze",
        15: "Quinze",
        16: "Dezesseis",
        17: "Dezessete",
        18: "Dezoito",
        19: "Dezenove",
        20: "Vinte",
    }

    cent = str(valor)
    cent = int(cent.split(".")[-1])
    
    if valor < 1:
        cent = int(valor * 100)
        if cent <= 20:
            return '{} centavo'.format(lista_valores[cent])
    else:
        pass
        #do something
        
    real = str(valor)
    real = int(cent.split(".")[0])
    
    if real <=20:
        return'
    
    
    
    
assert(cheque(0.01) == 'Um centavo')
assert(cheque(0.02) == 'Dois centavo')
assert(cheque(0.10) == 'Dez centavo')
assert(cheque(0.14) == 'Quatorze centavo')
assert(cheque(0.20) == 'Vinte centavo')
assert(cheque(10.0) == 'Dez reais')