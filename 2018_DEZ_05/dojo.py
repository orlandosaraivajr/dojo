digitos = {
    'um': 1,
    'dois': 2,
    'três': 3,
    'quatro': 4,
    'cinco': 5,
    'seis': 6,
    'sete': 7,
    'oito': 8,
    'nove': 9,
    'dez': 10,
    'onze': 11,
    'doze': 12,
    'treze': 13,
    'quatorze': 14,
    'quinze': 15,
    'dezesseis': 16,
    'dezessete': 17,
    'dezoito': 18,
    'dezenove': 19,
    'vinte': 20,
    'trinta': 30,
    'quarenta': 40,
    'cinquenta': 50,
    'sessenta': 60,
    'setenta': 70,
    'oitenta': 80,
    'noventa': 90,
    'cem': 100,
    'cento': 100,
    'duzentos': 200,
    'trezentos': 300,
    'quatrocentos': 400,
    'quinhentos': 500,
    'seiscentos': 600,
    'setecentos': 700,
    'oitocentos': 800,
    'novecentos': 900,
}


def converte_texto(texto):
    numero = 0
    subvalores = texto.split(" ")
    for valor in subvalores:
        texto = valor.strip()
        numero += digitos.get(texto, 0)
    return numero


def valor_cheque(valor_preenchido):
    if "real" in valor_preenchido:
        partes = valor_preenchido.split("real")
    else:
        partes = valor_preenchido.split("reais")

    num = "0"
    centavos = "0"
    if len(partes) > 1:
        subvalores = partes[0].split("mil")
        if len(subvalores) > 1:
            num = converte_texto(subvalores[0])
            num = num * 1000
            num = num + converte_texto(subvalores[1])
        else:
            num = converte_texto(subvalores[0])
        partes[0] = partes[1]

    centavos = converte_texto(partes[0])

    num = str(num)
    if centavos >= 10:
        centavos = str(centavos)
    else:
        centavos = '0' + str(centavos)
    num = num + ',' + centavos
    return num


assert(valor_cheque('dois mil reais') == '2000,00')
assert(valor_cheque('dois mil e quinhentos reais') == '2500,00')
assert(valor_cheque('trinta e três mil reais') == '33000,00')
assert(valor_cheque('trinta e três mil novecentos e noventa \
 e nove reais') == '33999,00')
assert(valor_cheque('quinhentos reais') == '500,00')
assert(valor_cheque('quinhentos e trinta e dois reais') == '532,00')
assert(valor_cheque('cento e vinte um reais') == '121,00')
assert(valor_cheque('novecentos e noventa e nove mil reais') == '999000,00')
assert(valor_cheque('novecentos e noventa e nove mil \
 reais e cinquenta centavos') == '999000,50')
assert(valor_cheque('cinquenta centavos') == '0,50')
assert(valor_cheque('um real e cinquenta centavos') == '1,50')
assert(valor_cheque('cinco centavos') == '0,05')
assert(valor_cheque('dez centavos') == '0,10')
assert(valor_cheque('quinze centavos') == '0,15')
