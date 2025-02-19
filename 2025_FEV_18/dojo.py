from enum import Enum

class Jokenpo(Enum):

    PEDRA = 'pedra'
    TESOURA = 'tesoura'
    PAPEL = 'papel'

REGRAS = {
    (Jokenpo.PEDRA, Jokenpo.TESOURA) : Jokenpo.PEDRA,
    (Jokenpo.TESOURA, Jokenpo.PAPEL) : Jokenpo.TESOURA,
    (Jokenpo.PAPEL, Jokenpo.PEDRA) : Jokenpo.PAPEL
}

def jokenpo(player1, player2):

    try:
        p1 = Jokenpo(player1)
        p2 = Jokenpo(player2)

#    if REGRAS[p1] == p2:
    #     return "Jogador 1 ganha"
    # else: 
    #     return "Jogador 2 ganha"

        if p1 == p2:
            return 'empate'

        return REGRAS.get((p1,p2), REGRAS.get(p1,p2)).value
    except ValueError:
        return 'Jogada invalida'
    # opcoes = ("pedra" , "papel", "tesoura")

    # if player1 not in opcoes or player2 not in opcoes:
    #    return "Jogada invalida"


    # if player1 == player2 :
    #     return 'empate'
    # elif player1 == 'papel' and player2 == 'pedra' or player1 == 'pedra' and player2 == 'papel' :
    #     return 'papel'
    # elif player1 == 'tesoura' and player2 == 'pedra' or player1 == 'pedra' and player2 == 'tesoura':
    #     return 'pedra'
    # elif player1 == 'tesoura' and player2 == 'papel'or player1 == 'papel' and player2 == 'tesoura':
    #     return 'tesoura'




assert jokenpo('pedra','papel') == 'papel'
assert jokenpo('pedra','pedra') == 'empate'
assert jokenpo('papel', 'pedra') == 'papel'
assert jokenpo('tesoura', 'pedra') == 'pedra'
assert jokenpo('pedra', 'tesoura') == 'pedra'
assert jokenpo('tesoura', 'papel') == 'tesoura' 
assert jokenpo('tesoura', 'tesoura') == 'empate'
assert jokenpo('papel', 'tesoura') == 'tesoura'
assert jokenpo('papel', 'papel') == 'empate'
assert jokenpo ('papel', 'bomba') =='Jogada invalida' 

'''
1 Orlando
2 Guilherme
3 Thiago Barros
4 Carlos
5 Pedro Beck
6 Pedro Otavio
7 Thiago Fumante

# Positivo
 - Importância dos testes unitários
 - Dojo remoto foi um sucesso
 - Trabalho em equipe
 - Interação entre os participantes
 - Refatoração de código
 - Trabalho sob pressão
 - Tempo de cinco minutos por ciclo
 - Uso das funções built-in do Python

# Pontos de Melhoria
 - Faltou inserir comentários
 - Dificuldades técnicas de acesso de alguns
 - Interpretador python não rodou dentro do VSCode
 
'''

