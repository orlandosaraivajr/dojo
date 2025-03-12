"""
#Ano Bissexto

A cada 4 anos, a diferença de horas entre o ano solar e o do calendário convencional completa cerca de 24 horas (mais exatamente: 23 horas, 15 minutos e 864 milésimos de segundo). Para compensar essa diferença e evitar um descompasso em relação às estações do ano, insere-se um dia extra no calendário e o mês de fevereiro fica com 29 dias. Essa correção é especialmente importante para atividades atreladas às estações, como a agricultura e até mesmo as festas religiosas.

Um determinado ano é bissexto se for divisível por 4, mas não divisível por 100, exceto se ele for também divisível por 400.

Exemplos:

São bissextos por exemplo:
1600
1732
1888
1944
2008
Não são bissextos por exemplo:
1742
1889
1951
2011
Escreva uma função que determina se um determinado ano informado é bissexto ou não.

Fonte: [http://dojopuzzles.com/problemas/exibe/ano-bissexto/]


1) Thiago Barros - 
2) Orlando - 
3) Pedro Otavio
4) Guilherme - 
5) 
6) 

Pontos Positivos
===================
- Terminamos o problema.
- Exploramos a função assert
- Trabalhamos melhor o conceito baby steps

Pontos de Melhorias
===================
- Mais participação
- Trabalhar a ideia de TDD
- Atualizar o VSCode. Não permite rodar python dentro do VSCode 



"""
def bissextos(numero):
    return ( numero % 4 ==0 and numero % 100 != 0) or (numero % 400 == 0)
        
def teste():        
    assert bissextos(1600)
    assert not bissextos(2011)
    assert bissextos(2024)
    assert bissextos(2000)
    assert bissextos(1732)
    assert not bissextos(2002)
    assert bissextos(4)
    assert not bissextos(1742)
    assert not bissextos(1889)
    assert not bissextos(1951)
    assert not bissextos(2011)
    print("todos passaram")

teste()

