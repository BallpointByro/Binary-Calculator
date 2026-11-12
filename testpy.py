def split(number):
    """Splits the number into binary digits, [128, 64, 32, 16, 8, 4, 2, 1]"""
    numberArray = number # work here
    return numberArray

if __name__ == "__main__":
    number = int(input("Number -> "))
    print(f"Number Specified in Binary would be: {bin(number)}")

    splitNumber = split(number)
    print(f"Number split! New number: {splitNumber}")
