# Dicionário de valores Romanos
roman_dict = {
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X',
    40: 'XL',
    50: 'L',
    90: 'XC',
    100: 'C',
    400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M'
}
    
def int_to_roman(num):
    # Lista de valores em ordem decrescente
    sorted_values = sorted(roman_dict.keys(), reverse=True)

    roman = ""
    for value in sorted_values:
        while num >= value:
            roman += roman_dict[value]
            num -= value
    return roman



assert int_to_roman(58) == "LVIII"
assert int_to_roman(158) == "CLVIII"

assert int_to_roman(1) == "I"
assert int_to_roman(4) == "IV"
assert int_to_roman(9) == "IX"

assert int_to_roman(10) == "X"
assert int_to_roman(40) == "XL"
assert int_to_roman(49) == "XLIX"
assert int_to_roman(90) == "XC"

assert int_to_roman(100) == "C"
assert int_to_roman(400) == "CD"
assert int_to_roman(500) == "D"
assert int_to_roman(900) == "CM"

assert int_to_roman(1000) == "M"
assert int_to_roman(1987) == "MCMLXXXVII"
assert int_to_roman(2024) == "MMXXIV"
assert int_to_roman(3999) == "MMMCMXCIX"  # maior número permitido com notação romana padrão

assert int_to_roman(44) == "XLIV"
assert int_to_roman(345) == "CCCXLV"
assert int_to_roman(888) == "DCCCLXXXVIII"