def nomeAutores(nome):
    
    sobrenomes_parente = ["FILHO", "FILHA", "NETO", "NETA", "SOBRINHO", "SOBRINHA" , "JUNIOR" ]
    primeiro_nome = nome.split()
    
    for name in nome.split(' '):
        if name in sobrenomes_parente:
            print(name)

    #if nome == '':
    #    return ''
    
    #nomesplit = nome.split(' ')
    
    #if len(nomesplit) == 1:
     #   return nome.upper
    
    #if len(nomesplit) == :
    #    return f('{nomesplit[1].upper}, {nomesplit[0]}')
    
    
    #da = ["da", "de", "do", "das", "dos"]
    #sobrenomes_parente = ["FILHO", "FILHA", "NETO", "NETA", "SOBRINHO", "SOBRINHA" , "JUNIOR" ]
    #for parente in sobrenomes_parente:
    #    if parente in nome:
    #        for d in da:
    #            if d in nome:
                    
    
    #print(nomesplit[0].upper())
    # if len(nomesplit) == 1:
    #     teste = nomesplit[0].upper()
    #     return teste
        
    #for name in nomesplit:
     #   print(name)
    
   # sobrenome = nomesplit[-1].upper()
   # nome = nomesplit[0].capitalize()
    
    

#assert nomeAutores('GUIMARAES') == 'GUIMARAES'
assert nomeAutores('manoel neto') == 'NETO, Manoel'
#assert nomeAutores('Manoel Jose da Silva Neto') == 'SILVA NETO, Manoel Jose da'
#assert nomeAutores('') == ''
