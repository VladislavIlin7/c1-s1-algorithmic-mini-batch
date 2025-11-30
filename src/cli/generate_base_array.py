from tests.test_cases.many_duplicates import many_duplicates
from tests.test_cases.nearly_sorted import nearly_sorted
from tests.test_cases.rand_int_array import rand_int_array
from tests.test_cases.reverse_sorted import reverse_sorted


def generate_base_array(choice: str, n: int) -> list[int] | None:
    """
    Базовая генерация массива целых чисел по выбору пользователя.
    Не знает ничего про конкретный алгоритм.
    """

    if choice == "2":
        # случайные и отрицательные, и положительные
        return rand_int_array(n, -10000, 10000)
    if choice == "3":
        return nearly_sorted(n, swaps=n // 10)
    if choice == "4":
        return many_duplicates(n)
    if choice == "5":
        return reverse_sorted(n)

    print("Неизвестный вариант")
    return None