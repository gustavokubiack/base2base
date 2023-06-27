class Hexadecimal:
    def __init__(self, num, base, convert_to):
        self.num = int(num, base)
        self.base = base
        self.convert_to = convert_to

    def hex_to_binary(self):
        return bin(self.num)[2:]

    def hex_to_octal(self):
        return oct(self.num)[2:]

    def hex_to_decimal(self):
        return self.num
