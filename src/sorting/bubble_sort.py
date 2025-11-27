from typing import Callable, Any, TypeVar

from src.exceptions.exceptions import CmpAndKeyTogetherError

T = TypeVar("T")


def bubble_sort(a: list[T],key: Callable[[T], Any] | None = None, cmp: Callable[[Any, Any], int] | None = None,) -> list[T]:
    """
    Сортировка пузырьком с поддержкой key и cmp
    key(x) -> ключ для сравнения
    cmp(a, b) -> отрицательное, если a<b; положительное, если a>b; 0 если равно
    """

    if key is not None and cmp is not None:
        raise CmpAndKeyTogetherError()

    n = len(a)
    if n <= 1:
        return a

    # key по умолчанию
    if key is None:
        key = lambda x: x

    # cmp по умолчанию (возвращает -1 / 0 / 1)
    if cmp is None:
        cmp = lambda x, y: (x > y) - (x < y)

    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if cmp(key(a[j]), key(a[j + 1])) > 0:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break

    return a
