# CAUTION: This code was written by an AI. Specifically Google Gemini.

import string

def convertToBase(num: int, base: int) -> str:
    if num == 0:
        return "0"

    digits = string.digits + string.ascii_uppercase

    result = ""
    isNegative = num < 0
    num = abs(num)

    while num > 0:
        remainder = num % base
        result = digits[remainder] + result
        num //= base

    return "-" + result if isNegative else result

number = int(input("Enter Base 10 (Denary) Number > "))

numberBinary = bin(number)[2:]
numberOctenary = oct(number)[2:]
numberHexadecimal = hex(number)[2:].upper()

numberB6 = convertToBase(number, 6)
numberB3 = convertToBase(number, 3)
numberB12 = convertToBase(number, 12)

print(f"""

NUMBER           : {number}
NUMBER (Binary)  : {numberBinary}
NUMBER (Octal)   : {numberOctenary}
NUMBER (Hex)     : {numberHexadecimal}
NUMBER (Base 6)  : {numberB6}
NUMBER (Base 3)  : {numberB3}
NUMBER (Base 12) : {numberB12}

""")
