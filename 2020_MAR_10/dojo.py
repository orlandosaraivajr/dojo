def abnt(nome_autor):
    nome = 'Orlando Saraiva do Nascimento'
    nome_separado = nome.split()
    sobrenome = nome_separado[-1].upper()
    primeiro_nome = nome_separado[0].capitalize()
    nome_final = sobrenome + ', ' + primeiro_nome
    return nome_final


    # nome_autor = nome_autor.split()
    #sobre = nome_autor[-1]
    #nome_autor.remove(sobre)
    #sobre = sobre.upper()
    #nome_autor = str(nome_autor)
    #nome_autor = nome_autor.capitalize()
    #return sobre + nome_autor'''





assert abnt('orlando saraiva do Nascimento') == 'NASCIMENTO, Orlando'
#assert abnt('fabio gomes suzarth junior') == 'SUZARTH JUNOR, Fabio Gomes'