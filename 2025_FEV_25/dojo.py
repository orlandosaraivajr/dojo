'''
Fonte: https://codingdojo.org/kata/NumbersInWords/

1) Orlando
2) Barros
3) Guilherme
4) Gabriel
5) Pedro Rufino

O que foi bom ?
----------------
- Interação foi melhor
- Baby Steps. Observamos a necessidade de fazer pouco a pouco
- Sempre podemos aprender
- Ter um desafio mais difícil foi legal

Pontos de Melhorias
-------------------
- Seguir uma única estratégia

'''

valores = {
    1: 'um',
    50: 'cinquenta', 
    }

def cheque(valor):
    listaValor = valor.split('.')

    nome = ""

    for num in listaValor:
        a = valores.get(int(num))
        if a:
            if nome == "":
                if a == 'um':
                    a = 'hum'
                nome += a
            else:
                nome += f' e {a}'
                
    return nome

# assert cheque(100.00) == 'cem reais'
assert cheque("1.50") == 'hum e cinquenta'