from src.base2base import Base2Base

def main():
    calculator = Base2Base()
    try:
        calculator.get_values()
        calculator.to_base_x()
    except:
        raise ValueError ("erro")


if __name__ == "__main__":
    main()
