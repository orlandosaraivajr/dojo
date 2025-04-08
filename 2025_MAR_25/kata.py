roman_dict = {
    1:'I',
    4: 'IV',
    5:'V',
    9: 'IX',
    10: 'X',
    40: 'XL',
    50: 'L',
    90: 'XC',
    100: 'C',
    400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M',
}

def int_to_roman(num):
    inner_list = sorted(roman_dict.keys(), reverse=True)
    roman = ''
    for value in inner_list:
        while num >= value:
            roman += roman_dict.get(value)
            num = num - value
    return roman

assert int_to_roman(58) == "LVIII" # 58 = 50 + 5 + 1 + 1 + 1
assert int_to_roman(158) == "CLVIII" # 158 = 100 + 50 + 5 + 1 + 1 + 1
# Unitários
assert int_to_roman(1) == "I"
assert int_to_roman(2) == "II"
assert int_to_roman(3) == "III"
assert int_to_roman(4) == "IV"
assert int_to_roman(5) == "V"
assert int_to_roman(6) == "VI"
assert int_to_roman(7) == "VII"
assert int_to_roman(8) == "VIII"
assert int_to_roman(9) == "IX"
# Dezenas
assert int_to_roman(10) == "X"
assert int_to_roman(20) == "XX"
assert int_to_roman(30) == "XXX"
assert int_to_roman(40) == "XL"
assert int_to_roman(50) == "L"
assert int_to_roman(60) == "LX"
assert int_to_roman(70) == "LXX"
assert int_to_roman(80) == "LXXX"
assert int_to_roman(90) == "XC"
# Centenas
assert int_to_roman(100) == "C"
assert int_to_roman(200) == "CC"
assert int_to_roman(300) == "CCC"
assert int_to_roman(400) == "CD"
assert int_to_roman(500) == "D"
assert int_to_roman(600) == "DC"
assert int_to_roman(700) == "DCC"
assert int_to_roman(800) == "DCCC"
assert int_to_roman(900) == "CM"
assert int_to_roman(1000) == "M"

assert int_to_roman(48) == "XLVIII"
assert int_to_roman(96) == "XCVI"
assert int_to_roman(448) == "CDXLVIII"
assert int_to_roman(1448) == "MCDXLVIII"
assert int_to_roman(2448) == "MMCDXLVIII"
