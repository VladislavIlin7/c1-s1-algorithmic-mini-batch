from typing import Callable, Any, TypeVar
from functools import cmp_to_key

from src.exceptions.exceptions import CmpAndKeyTogetherException

T = TypeVar("T")


def max_heapify(a: list[T], size: int, i: int, key: Callable[[T], Any]) -> None:
    """
    Просеивает элемент вниз в двоичной куче

    Используется для восстановления свойств max-heap
    """
    while True:
        l = 2 * i + 1
        r = 2 * i + 2
        largest = i

        if l < size and key(a[l]) > key(a[largest]):
            largest = l
        if r < size and key(a[r]) > key(a[largest]):
            largest = r
        if largest == i:
            break

        a[i], a[largest] = a[largest], a[i]
        i = largest


def heap_sort(
    a: list[T],
    key: Callable[[T], Any] | None = None,
    cmp: Callable[[T, T], int] | None = None,
) -> list[T]:
    """
    Сортировка на куче для элементов которые можно сравнить напрямую или через key или cmp

    :param a: список элементов одного типа
    :param key: функция получения ключа сортировки
    :param cmp: функция сравнения двух элементов
    :return: новый отсортированный список
    """

    if key is not None and cmp is not None:
        raise CmpAndKeyTogetherException()

    if not a:
        return []

    if cmp is not None:
        key = cmp_to_key(cmp)
    if key is None:
        key = lambda x: x  # type: ignore[assignment]

    arr = a.copy()
    size = len(arr)

    # строим кучу
    for i in range(size // 2 - 1, -1, -1):
        max_heapify(arr, size, i, key)

    # сортируем
    for end in range(size - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        size -= 1
        max_heapify(arr, size, 0, key)

    return arr
