def jokempo(player1, player2):
    if player1 == 'pedra' and player2 =='tesoura':
        return 'pedra' 
    elif player1 == player2 :
        return 'empate'
    elif player1 == "pedra" and player2 == "papel":
        return 'papel'
    elif player1 == "tesoura" and player2 == "pedra":
        return "pedra"
    elif player1 == "tesoura" and player2 == "papel":
        return "tesoura"
    elif player1 == "papel" and player2 == "tesoura":
        return "tesoura"
    elif player1 == "papel" and player2 == "pedra":
        return "papel"
    
    
'''Player 1 = Pedra'''
assert jokempo('pedra','papel') == 'papel'
assert jokempo('pedra','tesoura') == 'pedra'
assert jokempo('pedra','pedra') == 'empate'

'''Player 1 = Tesoura'''
assert jokempo('tesoura', 'papel') == 'tesoura'
assert jokempo('tesoura', 'tesoura') == 'empate'
assert jokempo('tesoura', 'pedra') == 'pedra'

'''Player 1 = Papel'''
assert jokempo('papel','pedra') == 'papel'
assert jokempo('papel', 'tesoura') == 'tesoura'
assert jokempo('papel','papel') == 'empate'


