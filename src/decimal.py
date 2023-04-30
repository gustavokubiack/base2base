class Decimal:

    def __init__(self, num, base, convert_to):
        self.num = num
        self.base = base 
        self.convert_to = convert_to

    def decimal_to_binary(self):
        if self.base == 10 and self.convert_to == 2:
            print (bin(self.num)[2:])

    def decimal_to_octal(self):
        if self.base == 10 and self.convert_to == 8:
            print (oct(self.num)[2:])
