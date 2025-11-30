from typing import Callable, Any

from src.sorting.comparators import cmp_abs, cmp_len


def choose_builtin_cmp() -> Callable[[Any, Any], int] | None:
    """
    Выбор одного из готовых компараторов.
    """
    while True:
        print("\nДоступные компараторы:")
        print("1 - cmp_abs  (сравнение по модулю целых чисел)")
        print("2 - cmp_len  (сравнение по длине строк)")
        print("0 - назад (без компаратора)")

        choice = input("> ").strip()
        if choice == "1":
            return cmp_abs
        if choice == "2":
            return cmp_len
        if choice == "0":
            return None
        print("Неизвестная команда, попробуйте ещё раз")