from src.decimal import Decimal
from src.octal import Octal

num = int(input("Insira um número: "))
base = int(input("Insira a base do número: "))
convert_to = int(input("Insira a base para conversão: "))


def main():
    decimal = Decimal(num, base, convert_to)
    octal = Octal(num, base, convert_to)
    """
    if convert_to == 2:
        print(decimal.decimal_to_binary())
    elif convert_to == 8:
        print(decimal.decimal_to_octal())
    elif convert_to == 16:
        print(decimal.decimal_to_hex())
    else:
        print(decimal.decimal_to_x())"""

    if base == 8 and convert_to == 10:
        print(octal.octal_to_decimal())
    elif base == 8 and convert_to == 2:
        print(octal.octal_to_binary())
    elif base == 8 and convert_to == 16:
        print(octal.octal_to_hex()())


if __name__ == "__main__":
    main()
