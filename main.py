from src.decimal import Decimal

num = int(input("Enter a number: "))
base = int(input("Enter a base: "))
convert_to = int(input("Enter a base to convert to: "))

def main():
    decimal = Decimal(num, base, convert_to)
    decimal.decimal_to_binary()
    decimal.decimal_to_octal()

if __name__ == "__main__":
    main()