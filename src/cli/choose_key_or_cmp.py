from typing import Callable, Any

from src.cli.choose_builtin_cmp import choose_builtin_cmp
from src.cli.read_custom_key import read_custom_key


def choose_key_or_cmp() -> None | tuple[Callable[[Any], Any], None] | tuple[None, Callable[[Any, Any], int]] | tuple[
    None, None]:
    """
    Диалог выбора: обычная сортировка / готовый cmp / свой key.
    Возвращает (key, cmp).
    """
    while True:
        print("\nКак сравнивать элементы?")
        print("1 - Обычное сравнение по значению (по умолчанию)")
        print("2 - Использовать готовый компаратор (cmp)")
        print("3 - Ввести свою функцию key")

        mode = input("> ").strip()

        if mode in {"1"}:
            return None, None

        if mode == "2":
            cmp = choose_builtin_cmp()
            if cmp is None:
                continue
            return None, cmp

        if mode == "3":
            key = read_custom_key()
            if key is None:
                continue
            return key, None

        print("Неизвестная команда, попробуйте ещё раз")