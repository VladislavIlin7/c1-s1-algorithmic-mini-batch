from typing import Callable, Any, TypeVar
from functools import cmp_to_key

from src.exceptions.exceptions import CmpAndKeyTogetherException

T = TypeVar("T")


def quick_sort(
    a: list[T],
    key: Callable[[T], Any] | None = None,
    cmp: Callable[[T, T], int] | None = None,
) -> list[T]:
    """
    Быстрая сортировка с поддержкой key или cmp

    Делит массив на части относительно опорного элемента и рекурсивно сортирует

    :param a: список элементов который нужно отсортировать
    :param key: функция получения ключа сортировки
    :param cmp: функция сравнения двух элементов
    :return: новый отсортированный список

    """

    if len(a) <= 1:
        return a

    if key is not None and cmp is not None:
        raise CmpAndKeyTogetherException()

    if cmp is not None:
        key = cmp_to_key(cmp)
    if key is None:
        key = lambda x: x  # type: ignore[assignment]

    pivot = a[len(a) // 2]
    pkey = key(pivot)

    left = [x for x in a if key(x) < pkey]
    middle = [x for x in a if key(x) == pkey]
    right = [x for x in a if key(x) > pkey]

    return quick_sort(left, key=key) + middle + quick_sort(right, key=key)
