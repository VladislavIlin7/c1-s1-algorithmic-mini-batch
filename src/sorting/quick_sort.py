from typing import Callable, Any, TypeVar
from functools import cmp_to_key

T = TypeVar("T")


def quick_sort(
    a: list[T],
    key: Callable[[T], Any] | None = None,
    cmp: Callable[[T, T], int] | None = None,
) -> list[T]:
    """Быстрая сортировка с поддержкой key ИЛИ cmp."""
    if len(a) <= 1:
        return a

    if key is not None and cmp is not None:
        raise ValueError("Нельзя одновременно использовать key и cmp")

    # если передали cmp – превращаем его в key
    if cmp is not None:
        key = cmp_to_key(cmp)

    # если вообще ничего не передали – key по умолчанию
    if key is None:
        key = lambda x: x  # type: ignore[assignment]

    pivot = a[len(a) // 2]
    pivot_key = key(pivot)

    left = [x for x in a if key(x) < pivot_key]
    middle = [x for x in a if key(x) == pivot_key]
    right = [x for x in a if key(x) > pivot_key]

    return (
        quick_sort(left, key=key)  # cmp уже "зашит" в key
        + middle
        + quick_sort(right, key=key)
    )