'''
Problema Jokempo
https://dojopuzzles.com/problems/jokenpo/

1) Orlando/ melhor aulak de terça
2) Pacolla 
3) val 
4) Case 
5) Maria Vitoria Suzarth
6) Case
7)valmir
8) 
9)

# Pontos Positivos
- Dojo remoto foi positivo
- Foi "da hora"
- Aprendizado colaborativo - piloto e copiloto ajudando
- Relembrar conceitos

# Pontos de melhorias
- Maior participação (!)
- Aumentar o nível do desafio
- Fazer baby steps
- 

'''

def jokempo(jogador1, jogador2):
    #Melhorar organizao -> case
    jogador1 = str(jogador1).capitalize()
    jogador2 = str(jogador2).capitalize()

    
    
    if (jogador1 == "Pedra"):
        if (jogador2 == "Papel"):
            return "Papel"
        elif (jogador2 == 'Tesoura'):
            return "Pedra"
            
    if (jogador1 == "Papel"):
        if (jogador2 == "Tesoura"):
            return "Tesoura"
        elif (jogador2 == "Pedra"):
            return "Papel"

    if (jogador1 == "Tesoura"):
        if (jogador2 == "Pedra"):
            return "Pedra"
        elif (jogador2 == "Papel"):
            return "Tesoura"
        
    if (jogador1 == jogador2): 
        return "Empate"

## Princial
assert jokempo('Pedra','Pedra')      == 'Empate'
assert jokempo('Pedra','Tesoura')    == 'Pedra'
assert jokempo('Pedra', 'Papel')     == 'Papel'
assert jokempo('Papel', 'Tesoura')   == 'Tesoura'
assert jokempo('Papel', 'Pedra')     == 'Papel'
assert jokempo('Papel', 'Papel')     == 'Empate'
assert jokempo('Tesoura', 'Pedra')   == 'Pedra'
assert jokempo('Tesoura', 'Papel')   == 'Tesoura'
assert jokempo('Tesoura', 'Tesoura') == 'Empate'
