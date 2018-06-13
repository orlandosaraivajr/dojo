dic = {"A": "2", "B": "22", "C": "222",
       "D": "3", "E": "33", "F": "333",
       "G": "4", "H": "44", "I": "444",
       "J": "5", "K": "55", "L": "555",
       "M": "6", "N": "66", "O": "666",
       "P": "7", "Q": "77", "R": "777", "S": "7777",
       "T": "8", "U": "88", "V": "888",
       "W": "9", "X": "99", "Y": "999", "Z": "9999",
       " ": "0"}


def sms(msg):
    response = ''
    for index in range(len(msg)):
        if index > 0:
            if test_char(msg[index - 1])[0] == test_char(msg[index])[0]:
                response += '_' + test_char(msg[index])
            else:
                response += test_char(msg[index])
        else:
            response += test_char(msg[index])
    return response


def test_char(char):
    return dic[char.upper()]


assert(test_char("A") == "2")
assert(test_char(" ") == "0")
assert(sms("a") == "2")
assert(sms("b") == "22")
assert(sms("c") == "222")
assert(sms("AD") == "23")
assert(sms("AB") == "2_22")
assert(sms("ab d") == "2_2203")
assert(sms("SEMPRE ACESSO O DOJOPUZZLES") ==
       "77773367_7773302_222337777_" +
       "777766606660366656667889999_9999555337777")
