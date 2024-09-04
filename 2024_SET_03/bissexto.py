"""
Fonte: https://dojopuzzles.com/problems/ano-bissexto/

1) Orlando
2) Luiza
3) Luana
4) Douglas
5) Daniel

Pontos Positivos

Teve resolução
Teve mais participação
Varios logicas diferentes para resolver um mesmo problema

Pontos de Melhorias
Testar outros métodos de teste kkk

"""
def bissexto(ano):
    if (ano % 4 == 0) and (ano % 100 != 0):
        return True
    if (ano % 400 == 0):
        return True
    return False


assert bissexto(1732) == True
assert bissexto(1888) == True
assert bissexto(1944) == True
assert bissexto(2008) == True
assert bissexto(1600) == True
assert bissexto(1500) == False
assert bissexto(1742) == False
assert bissexto(1889) == False
assert bissexto(1951) == False
assert bissexto(2011) == False
assert bissexto(300) == False
assert bissexto(100) == False
assert bissexto(3000) == False
assert bissexto(2024) == True

