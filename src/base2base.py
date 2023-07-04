class Base2Base:
    def __init__(self):
        self.number = None
        self.base = None
        self.convert_to = None

    def get_values(self):
        self.number = int(input("Informe o número: "))
        self.base = int(input("Insira a base do número: "))
        self.convert_to = int(input("Informe a base para converter: "))

    def to_decimal(self):
        decimal_number = 0
        power = 0
        temp_number = self.number

        while temp_number > 0:
            digit = temp_number % 10 
            decimal_number += digit * pow(self.base, power) 
            temp_number //= 10
            power += 1

        return decimal_number

    def to_base_x(self):
        decimal_number = self.to_decimal()
        base_x_number = ""
        base_digits = "0123456789ABCDEF"

        if decimal_number == 0:
            base_x_number = "0"
        else:
            while decimal_number > 0:
                digit = decimal_number % self.convert_to
                base_x_number = base_digits[digit] + base_x_number
                decimal_number //= self.convert_to

        return base_x_number


calc = Base2Base()
calc.get_values()
print(calc.to_base_x())