'''
1) Orlando
2) Diego
3) Klayvert
4) Gleison 
5) Rubens
'''

import re

# \W* é uma expressão regular que remove todo e qualquer caractere especial
# \s* é uma outra expressão regular que removo todo e qualquer espaço vazio

def palindrome(str_input):
    str_input = re.sub(r'\W*\s*', '', str_input.lower()).lower()
    
    if len(str_input) > 0:
        if str_input == str_input[::-1]:
            return True

    return False

str_input = "A man, a plan, a canal: Panama"
assert ( palindrome(str_input))
str_input2 = "Not Palindrome"
assert (not palindrome(str_input2))
str_input3 = "Race a car"
assert (not palindrome(str_input3))
str_input4 = " "
assert (not palindrome(str_input4))
str_input5 = "subi no onibus"
assert (palindrome(str_input5))
str_input6 = "12321"
assert palindrome(str_input6)

str_input7 = "A cara rajada da jararaca."
assert palindrome(str_input7)
str_input8 = "Ame o poema."
assert palindrome(str_input8)
str_input9 = "A grama é amarga."
assert palindrome(str_input9)
str_input10 = "A mala nada na lama."
assert palindrome(str_input10)
str_input11 = "A Rita pale para o Papa."
assert not palindrome(str_input11)
str_input12 = "A sacada da casa."
assert palindrome(str_input12)
str_input13 = "Luz azul"
assert palindrome(str_input13)