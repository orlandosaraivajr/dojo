class CPF:
    def num_cpf(numero):
        # verifica se a conversão é possível
        try:
            numero = str(numero)
        except:
            return None

        # verifica se só há números na string
        try:
            int(numero)
        except:
            return None

        # verifica o tamanho
        if len(numero) != 11:
            return None

        # retorna no formato desejado
        return "{}.{}.{}-{}".format(
            numero[0:3],
            numero[3:6],
            numero[6:9],
            numero[9:]
        )

    def cpf_num(cpf):
        saida = cpf.replace("-", "")
        saida = saida.replace(".", "")

        for x in saida:
            try:
                int(x)
            except:
                return None

        return saida


assert(CPF.num_cpf("31710105844") == "317.101.058-44")
assert(CPF.cpf_num("317.101.058-44") == "31710105844")
assert(CPF.num_cpf(31710105844) == "317.101.058-44")
assert(CPF.num_cpf(71515151515) == "715.151.515-15")
assert(CPF.num_cpf(7151515151.5) is None)
assert(CPF.num_cpf(71515151515555) is None)
assert(CPF.num_cpf('3171010584a') is None)
assert(CPF.cpf_num("317.101.058-4a") is None)
assert(CPF.cpf_num("317.101.058_44") is None)
assert(CPF.cpf_num("317.101.058_44123") is None)
assert(CPF.cpf_num("317.101.0584 1") is None)
