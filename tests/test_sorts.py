import random
import pytest

from src.sorting.bubble_sort import bubble_sort
from src.sorting.bucket_sort import bucket_sort
from src.sorting.counting_sort import counting_sort
from src.sorting.heap_sort import heap_sort
from src.sorting.quick_sort import quick_sort
from src.sorting.radix_sort import radix_sort
from tests.test_keys.many_duplicates import many_duplicates
from tests.test_keys.nearly_sorted import nearly_sorted
from tests.test_keys.rand_float_array import rand_float_array
from tests.test_keys.rand_int_array import rand_int_array
from tests.test_keys.reverse_sorted import reverse_sorted

SORTS = [
    bubble_sort,
    heap_sort,
    quick_sort,
    counting_sort,
    radix_sort,
    bucket_sort,
]

SORTS_FLOAT = [
    bubble_sort,
    bucket_sort,
    heap_sort,
    quick_sort,
]


@pytest.mark.repeat(5)
@pytest.mark.parametrize("func", SORTS_FLOAT)
def test_sorts_float_random(func):
    n = random.randint(1, 500)

    # 0. случайные вещественные
    arr = rand_float_array(n, 0, 300)
    arr_copy = arr.copy()
    assert func(arr_copy) == sorted(arr)


@pytest.mark.repeat(5)
@pytest.mark.parametrize("func", SORTS)
def test_sorts_int_random(func):
    n = random.randint(1, 500)

    # 1. случайные целочисленные
    arr = rand_int_array(n, 0, 300)
    arr_copy = arr.copy()
    assert func(arr_copy) == sorted(arr)

    # 2. много дублей
    arr = many_duplicates(n)
    arr_copy = arr.copy()
    assert func(arr_copy) == sorted(arr)

    # 3. почти отсортированные
    swaps = random.randint(0, n)
    arr = nearly_sorted(n, swaps)
    arr_copy = arr.copy()
    assert func(arr_copy) == sorted(arr)

    # 4. обратный порядок
    arr = reverse_sorted(n)
    arr_copy = arr.copy()
    assert func(arr_copy) == sorted(arr)
