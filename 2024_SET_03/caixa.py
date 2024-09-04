'''
Fonte: https://dojopuzzles.com/problems/caixa-eletronico/

1) Luana
2) Luiza
3) Frank
4)

Pontos Positivos
Desafio legal para várias lógicas
deu para discutir diferentes estruturas com esse desafio

Pontos de Melhoria
Mais interações
Estabelecer incentivos para participação

'''

def saque(valor):
    notas = [100, 50, 20, 10]
    resultado = {100: 0, 50: 0, 20: 0, 10: 0}

    for nota in notas:
        while valor >= nota:
            valor = valor - nota
            resultado[nota] = resultado[nota] + 1

    return resultado

assert saque(30) == {100: 0, 50: 0, 20: 1, 10: 1}
assert saque(80) == {100: 0, 50: 1, 20: 1, 10: 1}
assert saque(200) == {100: 2, 50: 0, 20: 0, 10: 0}
assert saque(150) == {50: 1, 100: 1, 20: 0, 10: 0}
assert saque(150) == {100: 1, 50: 1, 20: 0, 10: 0}