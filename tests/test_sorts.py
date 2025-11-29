import random
import pytest

from src.constants import SORTS_FLOAT, ALL_SORTS
from tests.test_cases.many_duplicates import many_duplicates
from tests.test_cases.nearly_sorted import nearly_sorted
from tests.test_cases.rand_float_array import rand_float_array
from tests.test_cases.rand_int_array import rand_int_array
from tests.test_cases.reverse_sorted import reverse_sorted


@pytest.mark.repeat(5)
@pytest.mark.parametrize("name, func", SORTS_FLOAT.items())
def test_sorts_float_random(name, func):
    n = random.randint(1, 500)

    # 0. случайные вещественные
    arr = rand_float_array(n, 0, 300)
    arr_copy = arr.copy()
    assert func(arr_copy) == sorted(arr)


@pytest.mark.repeat(5)
@pytest.mark.parametrize("name, func", ALL_SORTS.items())
def test_sorts_int_random(name, func):
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
