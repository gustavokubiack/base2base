class Binary:
    def __init__(self, num, base, convert_to):
        self.num = num
        self.base = base
        self.convert_to = convert_to

    def binary_to_decimal(self):
        return int(str(self.num), 2)

    def binary_to_octal(self):
        return oct(int(str(self.num), 2))[2:]

    def binary_to_hex(self):
        return hex(int(str(self.num), 2))[2:]
