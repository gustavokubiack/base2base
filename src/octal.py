class Octal:
    def __init__(self, num, base, convert_to):
        self.num = num
        self.base = base
        self.convert_to = convert_to

    def octal_to_binary(self):
        return bin(int(str(self.num), 8))[2:]

    def octal_to_decimal(self):
        return oct(self.num)[:2]

    def octal_to_hex(self):
        return hex(int(str(self.num), 8))[2:]
