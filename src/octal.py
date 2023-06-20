class Octal:
    def __init__(self, num, base, convert_to):
        self.num = num
        self.base = base
        self.convert_to = convert_to

    def octal_to_binary(self):
        if self.base == 8 and self.convert_to == 2:
            return bin(int(str(self.num), 8))[2:]

    def octal_to_decimal(self):
        if self.base == 8 and self.convert_to == 10:
            return oct(self.num)[:2]    
            