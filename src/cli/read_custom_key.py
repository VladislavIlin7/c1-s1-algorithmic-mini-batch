from typing import Callable, Any


def read_custom_key() -> Callable[[Any], Any] | None:
    """
    Выбор key-функции без eval:
    - обычное значение
    - модуль (abs)
    - остаток по модулю k
    - длина (для строк)
    - последняя цифра
    """
    while True:
        print("\nВыберите функцию key:")
        print("1 - Обычное значение (lambda x: x)")
        print("2 - Модуль числа (lambda x: abs(x))")
        print("3 - Остаток по модулю k (lambda x: x % k)")
        print("4 - Длина (для строк) (lambda x: len(x))")
        print("5 - Последняя цифра (lambda x: x % 10)")

        choice = input("> ").strip()

        if choice == "1":
            return lambda x: x

        if choice == "2":
            return lambda x: abs(x)

        if choice == "3":
            try:
                k = int(input("Введите k (целое число > 0): ").strip())
            except ValueError:
                print("Нужно ввести целое число")
                continue

            if k <= 0:
                print("k должно быть > 0")
                continue

            return lambda x, m=k: x % m

        if choice == "4":
            return lambda x: len(x)

        if choice == "5":
            return lambda x: x % 10

        print("Неизвестный вариант, попробуйте ещё раз")