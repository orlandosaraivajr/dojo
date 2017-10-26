def jogo(jogador1,jogador2):
    allowed_objects = set(['pedra','papel','tesoura'])
    jogadas = set([jogador1, jogador2])

    if not(jogador1  in allowed_objects and\
            jogador2 in allowed_objects):
        return None

    if jogador1 == jogador2:
        return "empate"

    if jogadas.issubset(['pedra','papel']):
        return 'papel'

    if jogadas.issubset(['tesoura', 'papel']):
        return 'tesoura'

    if jogadas.issubset(['tesoura', 'pedra']):
        return 'pedra'
    

assert(jogo("tesoura","papel")) == "tesoura"
assert(jogo("papel","tesoura")) == "tesoura"
assert(jogo("tesoura","pedra")) == "pedra"

assert(jogo("pedra", "tesoura")) == "pedra"
assert(jogo("tesoura", "papel")) == "tesoura"
assert(jogo("pedra", "papel")) == "papel"
assert(jogo("papel", "pedra")) == "papel"

assert(jogo("tesoura","tesoura")) == "empate"
assert(jogo("papel","papel")) == "empate"
assert(jogo("pedra", "pedra")) == "empate"

#momento zueira
assert(jogo("arma nuclear", "arma nuclear")) == None
assert(jogo("arma nuclear", "tesoura")) == None
assert(jogo("tesoura", "arma nuclear")) == None

