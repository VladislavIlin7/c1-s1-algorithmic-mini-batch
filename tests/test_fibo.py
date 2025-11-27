import pytest

from src.algorithms.fibo import fibo
from src.algorithms.fibo_recursive import fibo_recursive


def test_simple_fibo():

    assert fibo(0) == 0
    assert fibo(1) == 1
    assert fibo(2) == 1
    assert fibo(5) == 5

def test_fibo_all_errors():

    with pytest.raises(TypeError):
        fibo('qwerty')

    with pytest.raises(ValueError):
        fibo(-52)

def test_simple_fibo_rec():

    assert fibo_recursive(0) == 0
    assert fibo_recursive(1) == 1
    assert fibo_recursive(2) == 1
    assert fibo_recursive(5) == 5

def test_fibo_rec_all_errors():

    with pytest.raises(TypeError):
        fibo_recursive('qwerty')

    with pytest.raises(ValueError):
        fibo_recursive(-52)