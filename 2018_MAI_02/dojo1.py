def bissexto(ano):
    div4 = ano % 4 == 0
    div100 = ano % 100 == 0
    div400 = ano % 400 == 0

    if div4 and not div100:
        return True
    if div400:
        return True
    return False


assert(bissexto(1600))
assert(bissexto(1732))
assert(bissexto(1888))
assert(bissexto(1944))
assert(bissexto(2000))
assert(bissexto(2008))
assert(not bissexto(1742))
assert(not bissexto(1889))
assert(not bissexto(1951))
assert(not bissexto(2011))
