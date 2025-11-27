import pytest

from src.sorting.bubble_sort import bubble_sort
from src.sorting.heap_sort import heap_sort
from src.sorting.quick_sort import quick_sort


def cmp_abs(a: int, b: int) -> int:
    return (abs(a) > abs(b)) - (abs(a) < abs(b))


@pytest.mark.parametrize("func", [bubble_sort, heap_sort, quick_sort])
def test_sort_with_cmp_abs(func):
    arr = [3, -10, 2, -1, 0]
    res = func(arr.copy(), cmp=cmp_abs)
    assert res == sorted(arr, key=abs)

# сделать больше проверок на cmp и сделать проверки на key