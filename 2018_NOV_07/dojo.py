class SSHProtocol:
    pass

class HTTPProtocol:
    def get_Host(self, protocolo):
        host = protocolo[7:10]
        if(host == 'www'):
            return host
        else:
            return ''


    def get_Dominio(self, protocolo):
        protocolo1 = protocolo.split(':')
        protocolo2 = protocolo1[1].split('/')
        if 'www' in protocolo2[2]:
            dominio = protocolo2[2][4:]
        else:
            dominio = protocolo2[2]

        return dominio

    def get_Path(self, protocolo):
        parametro1 = protocolo.split(':')
        parametro2 = parametro1[1].split('/')
        parametro3 = parametro2[3:]
        path = ''
        for item in parametro3:
            if '=' not in item and item is not '':
                path += item + '/'

        return path

    def get_Parametro(self, protocolo):
        parametro1 = protocolo.split(':')
        parametro2 = parametro1[1].split('/')
        parametro3 = parametro2[3:]
        parametro = ''

        for item in parametro3:
            if '=' in item and item is not '':
                parametro += item

        return parametro

def analizer(protocolo):
    protocolos_validos = ['http','ssh']
    protocolo_recebido = protocolo.split(':')[0]

    for x in protocolos_validos:
        if(x == protocolo_recebido):
            return protocolo_recebido

    return ''

p1 = 'http://www.google.com/mail/user=fulano'
p2 = 'ssh://fulano%senha@git.com/'
p3 = 'invalid_url'
p4 = 'http://dojopuzzles.com/problemas/exibe/analisando-urls/'
p5 = 'http://www.google.com/mail/user=fulano;pass=123'

assert(analizer(p1) == 'http')
assert(analizer(p2) == 'ssh')
assert(analizer(p3) == '')
assert(analizer(p4) == 'http')

http = HTTPProtocol()
assert(http.get_Host(p1) == 'www')
assert(http.get_Host(p4) == '')
assert(http.get_Dominio(p1) == 'google.com')
assert(http.get_Dominio(p4) == 'dojopuzzles.com')

assert(http.get_Path(p1) == 'mail/')
assert(http.get_Path(p4) == 'problemas/exibe/analisando-urls/')

assert(http.get_Parametro(p1) == 'user=fulano')
assert(http.get_Parametro(p4) == '')
assert(http.get_Parametro(p5) == 'user=fulano;pass=123')


