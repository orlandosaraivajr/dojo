'''
Problem: Jokenpo
https://dojopuzzles.com/problems/jokenpo/

1) Orlando
2) Wilson
3) Kalliel
4) Bruno
'''

regras = {
    "Pedra":["Tesoura"],
    "Papel":["Pedra"],
    "Tesoura":["Papel"],
}

def jokenpo_2(jogador1, jogador2):
    if jogador1 not in regras:
      return "Jogador 1 inválido!"
    if jogador2 not in regras: 
      return "Jogador 2 inválido!"
    
    if jogador1 == jogador2:
        return "Empate"
    
    return "Jogador 1 venceu" if jogador2 in regras[jogador1] else 'Jogador 2 venceu'
        
        

def jokenpo(jogador1, jogador2):
    if jogador1 == 'Pedra' and jogador2 == 'Tesoura':
        return 'Pedra'
    if jogador1 == 'Papel' and jogador2 == 'Tesoura':
        return 'Tesoura'
    return 'Empate'

assert jokenpo('Pedra','Pedra') == 'Empate'
assert jokenpo('Papel', 'Papel') == 'Empate'
assert jokenpo('Tesoura', 'Tesoura') == 'Empate'
assert jokenpo('Pedra','Tesoura') == 'Pedra'
assert jokenpo('Papel','Tesoura') == 'Tesoura'

assert jokenpo_2('Pedra','Pedra') == 'Empate'
assert jokenpo_2('Papel', 'Papel') == 'Empate'
assert jokenpo_2('Tesoura', 'Tesoura') == 'Empate'
assert jokenpo_2('Pedra','Tesoura') == 'Jogador 1 venceu'
assert jokenpo_2('Papel','Tesoura') == 'Jogador 2 venceu'

assert jokenpo_2('Tesoura','Pedra') == 'Jogador 2 venceu'
assert jokenpo_2('Tesoura','Papel') == 'Jogador 1 venceu'

assert jokenpo_2('Mamona', 'Pedra') == 'Jogador 1 inválido!'
assert jokenpo_2('Pedra', 'Mamona') == 'Jogador 2 inválido!'

