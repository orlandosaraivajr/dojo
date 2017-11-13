def extrairDigito(valor):
	return [int(x) for x in str(valor) if x != "."]

def preenche(valor):
	valor_real = int(valor)
	valor_centavos = int((valor - valor_real) * 100)


	#1a estrategia
	#unidades1 = ["","um", "dois","três", "quatro", "cinco","seis","sete","oito", "nove"]
	#dezenas1  = ["", "dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta","noventa"]
	#2a estrategia
	unidades2 =["zero","um", "dois","três", "quatro", "cinco","seis","sete","oito", "nove","dez","onze","doze","treze","quatorze","quinze","dezesseis","dezessete","dezoito","dezenove"]
	dezenas2  = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta","noventa"]

	texto = ""
	#digitos = extrairDigito(valor_centavos*10)
	#print(digitos)

	if valor_real < 20:
		texto  += unidades2[valor_real]
	
	if valor_centavos < 20:
		texto  += unidades2[valor_centavos]
	elif valor_centavos < 100:
		texto += dezenas2[valor_centavos//10]


	if (digitos[-2] > 2):
		#2a extrategia
		texto = texto + unidades2[int(valor_centavos*10)]
	else:
		#1a estrategia
		texto = texto + dezenas1[digitos[-2]]
		texto = texto + unidades1[digitos[-1]]

	texto = texto + " centavos"
	print(texto)


	return texto

assert(preenche(0.05)=="cinco centavos")
assert(preenche(0.10)=="dez centavos")
assert(preenche(0.00)=="zero centavos")
assert(preenche(0.15)=="quinze centavos")
assert(preenche(0.23)=="vinte e três centavos")