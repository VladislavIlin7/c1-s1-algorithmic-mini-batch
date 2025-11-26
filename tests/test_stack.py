import pytest

from src.structures.stack import Stack
from src.exceptions.exceptions import StackIsEmptyError


def test_basic_push_pop():
    s = Stack()

    assert s.is_empty()
    assert len(s) == 0

    s.push(1)
    s.push(2)
    s.push(3)

    assert not s.is_empty()
    assert len(s) == 3
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.is_empty()
    assert len(s) == 0


def test_min_simple():
    s = Stack()

    s.push(5)
    s.push(3)
    s.push(7)
    s.push(3)

    assert s.min() == 3

    s.pop()
    assert s.min() == 3

    s.pop()
    assert s.min() == 3

    s.pop()
    assert s.min() == 5


def test_peek():
    s = Stack()

    s.push(10)
    s.push(20)

    assert s.peek() == 20
    assert not s.is_empty()
    assert len(s) == 2
    assert s.pop() == 20
    assert s.pop() == 10


def test_errors_on_empty():
    s = Stack()

    with pytest.raises(StackIsEmptyError):
        s.pop()

    with pytest.raises(StackIsEmptyError):
        s.peek()

    with pytest.raises(StackIsEmptyError):
        s.min()
