from functools import cmp_to_key
from typing import Callable, Any, TypeVar
import copy

from src.exceptions.exceptions import CmpAndKeyTogetherException

T = TypeVar("T")


def bubble_sort(
        a: list[T],
        key: Callable[[T], Any] | None = None,
        cmp: Callable[[T, T], int] | None = None,
) -> list[T]:
    """
    Сортировка пузырьком O(n^2)

    :param a: список элементов одного типа
    :param key: функция получения ключа сравнения
    :param cmp: функция сравнения двух элементов
    :return: новый отсортированный список

    """

    if key is not None and cmp is not None:
        raise CmpAndKeyTogetherException()

    if cmp is not None:
        key = cmp_to_key(cmp)

    if key is None:
        key = lambda x: x  # type: ignore[assignment]

    result = copy.deepcopy(a)
    n = len(result)

    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if key(result[j]) > key(result[j + 1]):
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break

    return result
