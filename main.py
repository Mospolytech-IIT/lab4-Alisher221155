from functions import *

def main():
    try:
        # Шаг 1: Вызов функций с выбрасыванием исключений без обработки
        print(divide_numbers(5, 0))
        print(check_positive_number(-4))
         
        # Шаг 2: Функция с обработкой общего исключения
        print(parse_integer("abc"))
        
        # Шаг 3: Функция с обработкой общего исключения и finally
        print(safe_square_root(-15))
        
        # Шаг 4: Функции с несколькими обработчиками исключений
        print(perform_operations(10, 0))
        
        # Шаг 5: Функция с генерацией и обработкой исключений
        print(validate_input("10a"))
        
        # Шаг 6: Пользовательские исключения
        print(check_custom_exceptions(-2))
        
        # Шаг 8: Дополнительные функции
        print(square("abc"))
        print(concatenate_strings("Hello, ", 123))
        print(factorial(-3))
        
    except Exception as e:
        print(f"Ошибка при выполнении main: {e}")

if __name__ == "__main__":
    main()
