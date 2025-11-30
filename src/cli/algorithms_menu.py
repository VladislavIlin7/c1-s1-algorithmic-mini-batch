from typing import Callable

from src.algorithms.factorial import factorial
from src.algorithms.factorial_recursive import factorial_recursive
from src.algorithms.fibo import fibo
from src.algorithms.fibo_recursive import fibo_recursive


def algorithms_menu() -> None:
    """
    Подменю для запуска алгоритмов:
    - факториал (итеративный и рекурсивный)
    - числа Фибоначчи (итеративный и рекурсивный)
    """

    while True:
        print("\n=== Меню алгоритмов ===")
        print("1 - factorial (итеративный)")
        print("2 - factorial_recursive (рекурсивный)")
        print("3 - fibo (итеративный)")
        print("4 - fibo_recursive (рекурсивный)")
        print("back / 0 - вернуться в главное меню")

        cmd = input("> ").strip()

        if cmd in {"back", "0"}:
            break

        if cmd not in {"1", "2", "3", "4"}:
            print("Неизвестная команда, попробуйте ещё раз")
            continue

        # читаем n
        try:
            n = int(input("Введите n (целое неотрицательное): ").strip())
        except ValueError:
            print("Нужно ввести целое число")
            continue

        func_name: str
        func: Callable[[int], int]

        if cmd == "1":
            func_name = "factorial"
            func = factorial
        elif cmd == "2":
            func_name = "factorial_recursive"
            func = factorial_recursive
        elif cmd == "3":
            func_name = "fibo"
            func = fibo
        else:
            func_name = "fibo_recursive"
            func = fibo_recursive

        # лёгкая защита от слишком больших рекурсий
        if func_name.endswith("_recursive") and n > 1000:
            print("Слишком большое n для рекурсивной реализации, выберите меньше или итеративный вариант.")
            continue

        try:
            result = func(n)
        except (TypeError, ValueError) as e:
            print(f"Ошибка: {e}")
            continue

        print(f"{func_name}({n}) = {result}")