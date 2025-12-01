import pytest

from src.sorting.bubble_sort import bubble_sort
from src.sorting.comparators import cmp_abs, cmp_len
from src.sorting.heap_sort import heap_sort
from src.sorting.quick_sort import quick_sort

TESTS_SORT_WIHT_KEY_OR_CMP = [bubble_sort, heap_sort, quick_sort]


@pytest.mark.parametrize("func", TESTS_SORT_WIHT_KEY_OR_CMP)
def test_sort_with_cmp_abs(func):
    arr = [3, -10, 2, -1, 0]
    res = func(arr.copy(), cmp=cmp_abs)
    assert res == [0, -1, 2, 3, -10]


@pytest.mark.parametrize("func", TESTS_SORT_WIHT_KEY_OR_CMP)
def test_sort_with_cmp_len(func):
    arr = ['xx', 'qwer', '12345', 'aa', 'bbb', 'aa']
    res = func(arr.copy(), cmp=cmp_len)
    print(res)
    assert res == ['aa', 'aa', 'xx', 'bbb', 'qwer', '12345']


@pytest.mark.parametrize("func", TESTS_SORT_WIHT_KEY_OR_CMP)
def test_sort_with_key_abs(func):
    arr = [3, -10, 2, -1, 0]
    res = func(arr.copy(), key=lambda x: abs(x))
    print(res)
    assert res == [0, -1, 2, 3, -10]


@pytest.mark.parametrize("func", TESTS_SORT_WIHT_KEY_OR_CMP)
def test_sort_with_key_len(func):
    arr = ['qwer', '12345', 'aa', 'bbb', 'aa']
    res = func(arr.copy(), key=lambda x: len(x))
    print(res)
    assert res == ['aa', 'aa','bbb', 'qwer', '12345']


@pytest.mark.parametrize("func", TESTS_SORT_WIHT_KEY_OR_CMP)
def test_sort_with_key_last_num(func):
    arr = [1234, 56, 978, 11]
    res = func(arr.copy(), key=lambda x: x % 10)
    print(res)
    assert res == [11, 1234, 56, 978]
