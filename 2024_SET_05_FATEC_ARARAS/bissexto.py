'''
Pontos Positivos
- Trabalho em equipe
- Novos participantes
- Entregamos o código rodando
- Refatorar o código

Pontos de Melhorias
- Desafios maiores e mais difíceis
- Live com outras Fatecs

'''

def bissexto(ano):
    if(ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0): 
        return True
    return False


assert bissexto(1600) == True
assert bissexto(1732) == True
assert bissexto(1888) == True
assert bissexto(1944) == True
assert bissexto(2008) == True
assert bissexto(1742) == False
assert bissexto(1889) == False
assert bissexto(1951) == False
assert bissexto(2011) == False
assert bissexto(16546546846871) == False
assert bissexto(400000000 * 10) == True