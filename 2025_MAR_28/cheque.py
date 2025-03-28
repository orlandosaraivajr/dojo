def cheque(valor):
    centavos = str(valor.split('.')[1])
    if centavos == '05':
        centavos = 'cinco'
    if centavos == '02':
        centavos= 'dois'
    if centavos == '50':
        centavos = 'cinquenta'
    return centavos + " centavos"


assert cheque('0.05') == 'cinco centavos'
assert cheque('0.02') == 'dois centavos'
assert cheque('0.50') == 'cinquenta centavos'