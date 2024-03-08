def abnt(nome_autor):
    nome = ""
    nome_abnt = nome_autor.split(' ')
    sobrenome= nome_abnt[-1].upper()
    for elemento in nome_autor:
        nome = (nome + elemento)
        if elemento == " ":
            break
    abnt = (sobrenome + ", " + nome)
    
                
    return abnt


#print(abnt('Fernando Claudiano da Silva'))

assert abnt("Joao Silva"), "SILVA, Joao"
assert abnt("Paulo Coelho"), "COELHO, Paulo"
