import pytest

from src.algorithms.factorial import factorial
from src.algorithms.factorial_recursive import factorial_recursive


def test_simple_fact():

    assert factorial(5) == 120
    assert factorial(0) == 1


def test_fact_all_error():

    with pytest.raises(TypeError):
        factorial('qwerty')

    with pytest.raises(ValueError):
        factorial(-52)


def test_simple_fact_rec():

    assert factorial_recursive(5) == 120
    assert factorial_recursive(0) == 1
    assert factorial_recursive(1) == 1
    assert factorial_recursive(2) == 2


def test_fact_rec_all_error():

    with pytest.raises(TypeError):
        factorial('qwerty')

    with pytest.raises(ValueError):
        factorial(-52)
