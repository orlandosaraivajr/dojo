# https://leetcode.com/problems/multiply-strings/description/
'''
def mult(num1, num2):
    num11 = int(num1)
    num22 = int(num2)
    num3 = num11 * num22
    return(str(num3))
'''

def mult(num1, num2):
    return str(int(num1)*int(num2))

assert mult(num1 = "2", num2 = "3") == "6"
assert mult(num1 = "123", num2 = "456") == "56088"
assert mult(num1 = "0", num2 = "456") == "0"
assert mult(num1 = "-123", num2 = "456") == "-56088"