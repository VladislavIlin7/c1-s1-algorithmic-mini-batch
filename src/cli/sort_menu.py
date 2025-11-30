from typing import Callable, Any

from src.cli.choose_array import choose_array
from src.cli.choose_key_or_cmp import choose_key_or_cmp
from src.constants import ALL_SORTS

SORTS_WITH_KEY_OR_CMP = {"bubble", "heap", "quick"}

def sort_menu() -> None:
    """
    Подменю для работы с сортировками
    """

    while True:
        print("\n=== Меню сортировок ===")
        print("Доступные алгоритмы:")

        for name in ALL_SORTS.keys():
            print(f"- {name}")

        print("Команды:")
        print("  <имя_алгоритма>  - отсортировать массив, например bubble")
        print("  back             - вернуться в главное меню")

        cmd = input("> ").strip()

        if cmd == "back":
            break

        algo_name = cmd

        if algo_name not in ALL_SORTS:
            print("Такой сортировки нет попробуйте ещё раз")
            continue

        algo = ALL_SORTS[algo_name]
        arr = choose_array(algo_name)

        if arr is None:
            # пользователь явно отменил выбор массива
            continue

        print(f"Исходный массив: {arr}")

        # выбор способа сравнения, если алгоритм поддерживает key / cmp
        key: Callable[[Any], Any] | None = None
        cmp: Callable[[Any, Any], int] | None = None

        if algo_name in SORTS_WITH_KEY_OR_CMP:
            key, cmp = choose_key_or_cmp()

        # вызов сортировки
        if key is not None or cmp is not None:
            result = algo(arr, key=key, cmp=cmp)  # type: ignore[arg-type]
        else:
            result = algo(arr)  # type: ignore[call-arg]

        print(f"Отсортированный массив: {result}")