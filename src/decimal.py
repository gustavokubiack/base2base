class Decimal:
    def __init__(self, num, base, convert_to):
        self.num = num
        self.base = base
        self.convert_to = convert_to

    def decimal_to_binary(self):
        return bin(self.num)[2:]

    def decimal_to_octal(self):
        return oct(self.num)[2:]

    def decimal_to_hex(self):
        return hex(self.num)[2:]

    def decimal_to_x(self):
        digits = []
        while self.num > 0:
            remainder = self.num % self.convert_to
            digits.append(remainder)
            self.num = self.num // self.convert_to
        digits.reverse()
        result = "".join(str(digit) for digit in digits)
        return result
