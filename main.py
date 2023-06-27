from src.decimal import Decimal
from src.octal import Octal
from src.binary import Binary
from src.hexadecimal import Hexadecimal


class Calculator:
    def __init__(self):
        self.num = None
        self.base = None
        self.convert_to = None

    def get_num(self):
        self.base = int(input("Insira a base do número: "))
        if self.base == 16:
            self.num = input("Insira um número: ")
        else:
            self.num = int(input("Insira um número: "))
        self.convert_to = int(input("Insira a base para conversão: "))
        return self.num, self.base, self.convert_to

    def calculate(self):
        conversions = {
            (2, 10): Binary(self.num, self.base, self.convert_to).binary_to_decimal,
            (2, 8): Binary(self.num, self.base, self.convert_to).binary_to_octal,
            (2, 16): lambda: Binary(self.num, self.base, self.convert_to)
            .binary_to_hex()
            .upper(),
            (10, 2): Decimal(self.num, self.base, self.convert_to).decimal_to_binary,
            (10, 8): Decimal(self.num, self.base, self.convert_to).decimal_to_octal,
            (10, 16): lambda: Decimal(self.num, self.base, self.convert_to)
            .decimal_to_hex()
            .upper(),
            (8, 2): Octal(self.num, self.base, self.convert_to).octal_to_binary,
            (8, 10): Octal(self.num, self.base, self.convert_to).octal_to_decimal,
            (8, 16): lambda: Octal(self.num, self.base, self.convert_to)
            .octal_to_hex()
            .upper(),
            (16, 2): Hexadecimal(self.num, self.base, self.convert_to).hex_to_binary,
            (16, 8): Hexadecimal(self.num, self.base, self.convert_to).hex_to_octal,
            (16, 10): Hexadecimal(self.num, self.base, self.convert_to).hex_to_decimal,
        }

        conversion_key = (self.base, self.convert_to)
        if conversion_key in conversions:
            conversion_method = conversions[conversion_key]
            return conversion_method()
        else:
            return "Conversão não suportada para as bases fornecidas."


calculador = Calculator()
calculador.get_num()
print(calculador.calculate())
