import pytest

from src.sorting.bubble_sort import bubble_sort
from src.sorting.comparators import cmp_abs, cmp_len
from src.sorting.heap_sort import heap_sort
from src.sorting.quick_sort import quick_sort




@pytest.mark.parametrize("func", [bubble_sort, heap_sort, quick_sort])
def test_sort_with_cmp_abs(func):
    arr = [3, -10, 2, -1, 0]
    res = func(arr.copy(), cmp=cmp_abs)
    assert res == [0, -1, 2, 3, -10]


# сделать больше проверок на cmp и сделать проверки на key
@pytest.mark.parametrize("func", [bubble_sort, heap_sort, quick_sort])
def test_sort_with_cmp_len(func):
    arr = ['xx', 'qwer', '12345', 'aa', 'bbb', 'aa']
    res = func(arr.copy(), cmp=cmp_len)
    print(res)
    assert res == ['aa','aa','xx', 'bbb', 'qwer', '12345']
