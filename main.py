class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "деление на ноль"
        return a / b

    def run(self):
        print("Доступные операции: +, -, *, /")

        while True:
            op = input("\nВведите операцию (+, -, *, /) или 'q' для выхода: ")

            if op == 'q':
                print("Выход из калькулятора")
                break

            if op not in ['+', '-', '*', '/']:
                print("Неверная операция!")
                continue

            try:
                a = float(input("Введите первое число: "))
                b = float(input("Введите второе число: "))
            except ValueError:
                print("Ошибка: введите корректные числа")
                continue

            if op == '+':
                print("Результат:", self.add(a, b))
            elif op == '-':
                print("Результат:", self.subtract(a, b))
            elif op == '*':
                print("Результат:", self.multiply(a, b))
            elif op == '/':
                print("Результат:", self.divide(a, b))

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
