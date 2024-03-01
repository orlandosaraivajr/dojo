def jokempo(jogador1, jogador2):
    regras = {
        Pedra:{"Pedra","Empate","Tesoura","Jogador 1 vence","Papel","Jogador 2 vence"}
        Papel:{"Papel","Empate","Pedra","Jogador 1 vence","Tesoura","Jogador 2 vence"}
        Tesoura:{"Tesoura","Empate","Papel","Jogador 1 vence","Pedra","Jogador 2 vence"}
    }
    resultado = regras.get{str(jogador1).lower().capitalize().}
    '''if {jogador1, jogador2} == {'Pedra', 'Papel'}:
        return 'Papel'
    if {jogador1, jogador2} == {'Pedra', 'Tesoura'}:
        return 'Pedra'
    if {jogador1, jogador2} == {'Tesoura', 'Papel'}:
        return 'Tesoura'
    if jogador1 == jogador2:
        return "Empate"'''
    
    '''
    if (jogador1 == 'Pedra' and jogador2 == 'Tesoura') or (jogador2 == 'Pedra' and jogador1 == 'Tesoura'):
        return 'Pedra'
    if (jogador1 =='Papel' and jogador2 == 'Pedra') or (jogador2 =='Papel' and jogador1 == 'Pedra'):
        return 'Papel'
    if (jogador1 == 'Papel' and jogador2 == 'Tesoura') or (jogador2 == 'Papel' and jogador1 == 'Tesoura'):
        return 'Tesoura'
    return "Empate"
    '''

assert(jokempo('Pedra','Pedra') == "Empate")
assert(jokempo('Papel','Papel') == "Empate")
assert(jokempo('Tesoura','Tesoura') == "Empate")
assert(jokempo('Pedra','Tesoura') == "Pedra")
assert(jokempo('Papel', 'Pedra') == "Papel")
assert(jokempo('Pedra', 'Papel') == "Papel")
assert(jokempo('Tesoura', 'Pedra') == "Pedra")
assert(jokempo('Papel', 'Tesoura') == 'Tesoura')
assert(jokempo('Tesoura', 'Papel') == 'Tesoura')