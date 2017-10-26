def juiz(jogador1, jogador2):
    if not (isinstance(jogador1, str) and isinstance(jogador2, str)):
        return "jogada invalida"

    jogador1 = jogador1.lower()
    jogador2 = jogador2.lower()

    if (jogador1 in("pedra","papel","tesoura")) and (jogador2 in("pedra", "papel", "tesoura")):  
        if jogador1 == jogador2:
            return "empate"

        if (jogador1 == "pedra" and jogador2 == "tesoura") or (jogador1=="tesoura" and jogador2=="pedra"):
            return "pedra"        

        if (jogador1 == "pedra" and jogador2 == "papel") or (jogador1=="papel" and jogador2=="pedra"):
            return "papel"
 
        if (jogador1 == "tesoura" and jogador2 == "papel") or (jogador1 == "papel" and jogador2 == "tesoura"):
            return "tesoura"

    else:
        return "jogada invalida"


    
#casos de empate
assert(juiz("pedra","pedra") == "empate")
assert(juiz("papel","papel") == "empate")
assert(juiz("tesoura","tesoura") == "empate")
#casos onde pedra ganha
assert(juiz("pedra","tesoura") == "pedra")
assert(juiz("tesoura","pedra") == "pedra")
#casos onde papel ganha
assert(juiz("pedra","papel") == "papel")
assert(juiz("papel","pedra") == "papel")
#casos onde tesoura ganha
assert(juiz("tesoura","papel") == "tesoura")
assert(juiz("papel","tesoura") == "tesoura")

assert(juiz("bomba","bomba")== "jogada invalida")

assert(juiz("TESOURA","PEDRA")== "pedra")    
assert(juiz("PEDRA", "TESOURA") == "pedra")
assert(juiz("PAPEL", "TESOURA") == "tesoura")
assert(juiz("TESOURA", "TESOURA") == "empate")
assert(juiz("t3sour4", "pedra") == "jogada invalida")
assert(juiz(1,2) == "jogada invalida")
assert(juiz([1, 2, 3], [4, 5, 6]) == "jogada invalida")

