class NegativeValueError(Exception):
    pass

class ZeroValueError(Exception):
    pass

class NonIntegerValueError(Exception):
    pass

def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Деление на ноль невозможно.")
    return a / b

def check_positive_number(num):
    if num < 0:
        raise ValueError("Число должно быть положительным.")
    return True

def parse_integer(value):
    try:
        return int(value)
    except Exception as e:
        print(f"Ошибка преобразования в целое число: {e}")

def safe_square_root(value):
    import math
    try:
        if value < 0:
            raise ValueError("Квадратный корень из отрицательного числа невозможен.")
        return math.sqrt(value)
    except Exception as e:
        print(f"Ошибка при вычислении квадратного корня: {e}")
    finally:
        print("Завершение вычисления квадратного корня.")

def perform_operations(a, b):
    try:
        result = a / b
        if a < 0 or b < 0:
            raise ValueError("Операнды должны быть положительными.")
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError("Операнды должны быть целыми числами.")
        return result
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль.")
    except ValueError as ve:
        print(f"Ошибка значения: {ve}")
    except TypeError as te:
        print(f"Ошибка типа данных: {te}")
    finally:
        print("Завершение операции.")

def validate_input(value):
    try:
        if not isinstance(value, str):
            raise TypeError("Входное значение должно быть строкой.")
        if not value.isdigit():
            raise ValueError("Строка должна содержать только цифры.")
        return int(value)
    except TypeError as te:
        print(f"Ошибка типа: {te}")
    except ValueError as ve:
        print(f"Ошибка значения: {ve}")
    finally:
        print("Проверка входного значения завершена.")

def square(value):
   
    if not isinstance(value, (int, float)):
        raise TypeError("Аргумент должен быть числом.")
    return value * value

def concatenate_strings(a, b):
   
    if not isinstance(a, str) or not isinstance(b, str):
        raise TypeError("Оба аргумента должны быть строками.")
    return a + b

def factorial(n):
   
    if not isinstance(n, int):
        raise TypeError("Значение должно быть целым числом.")
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определён.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def check_custom_exceptions(value):
    try:
        if value < 0:
            raise NegativeValueError("Отрицательное значение недопустимо.")
        elif value == 0:
            raise ZeroValueError("Нулевое значение недопустимо.")
        elif not isinstance(value, int):
            raise NonIntegerValueError("Значение должно быть целым числом.")
        return True
    except (NegativeValueError, ZeroValueError, NonIntegerValueError) as e:
        print(f"Ошибка: {e}")
    finally:
        print("Проверка пользовательских исключений завершена.")
