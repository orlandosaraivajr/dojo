"""
1 - Orlando
2 - Diego
3 - Klayvert
4 - Orlando
"""

def jokenpo(jogador1, jogador2):
    regras = {
        'Pedra': {'Pedra': 'Empate', 'Papel': 'Jogador 2 vence', 'Tesoura': 'Jogador 1 vence'},
        'Papel': {'Pedra': 'Jogador 1 vence', 'Papel': 'Empate', 'Tesoura': 'Jogador 2 vence'},
        'Tesoura': {'Pedra': 'Jogador 2 vence', 'Papel': 'Jogador 1 vence', 'Tesoura': 'Empate'}
    } 
    resultado = regras.get(str(jogador1).lower().capitalize(),{}).get(str(jogador2).lower().capitalize(),'Erro')

    return resultado

assert(jokenpo("Pedra","Pedra") == "Empate")
assert(jokenpo("Pedra","Tesoura") == 'Jogador 1 vence')
assert(jokenpo("Pedra","Tesoura") == 'Jogador 1 vence')
assert(jokenpo("Tesoura","Pedra") == 'Jogador 2 vence')

assert(jokenpo('Tesoura', 'Pedra') == 'Jogador 2 vence')
assert(jokenpo('Pedra', 'Papel') == 'Jogador 2 vence')
assert(jokenpo('Papel', 'Tesoura') == 'Jogador 2 vence')

assert(jokenpo("Papel","Papel") == 'Empate')
assert(jokenpo("Papel","Papel") == 'Empate')
assert(jokenpo("Tesoura","Tesoura") == 'Empate')
assert(jokenpo("Soco inglês","Tesoura") == 'Erro')
assert(jokenpo("Tesoura","Taco") == 'Erro')
assert(jokenpo("Tesoura",12) == 'Erro')
