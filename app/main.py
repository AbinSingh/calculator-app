from app.calculator import Calculator

if __name__ == "__main__":
    calc = Calculator()
    print("Calculator Demo")
    print("Add: 5 + 3 =", calc.add(5, 3))
    print("Subtract: 5 - 3 =", calc.subtract(5, 3))
    print("Multiply: 5 * 3 =", calc.multiply(5, 3))
    print("Divide: 5 / 3 =", calc.divide(5, 3))