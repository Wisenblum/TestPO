class CalculatorTypeError(Exception):
    """Ошибка: неверный тип данных"""
    pass

class CalculatorDivideByZeroError(Exception):
    """Ошибка: деление на ноль"""
    pass


class Calculator:
    def _check(self, a, b):
        # Проверяем, что оба числа int или float (и не bool)
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise CalculatorTypeError("Можно использовать только числа")
        if isinstance(a, bool) or isinstance(b, bool):
            raise CalculatorTypeError("Булевы значения не допускаются")

    def add(self, a, b):
        self._check(a, b)
        return a + b

    def subtract(self, a, b):
        self._check(a, b)
        return a - b

    def multiply(self, a, b):
        self._check(a, b)
        return a * b

    def divide(self, a, b):
        self._check(a, b)
        if b == 0:
            raise CalculatorDivideByZeroError("Деление на ноль запрещено")
        return a / b
