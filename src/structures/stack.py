from src.exceptions.exceptions import StackIsEmptyException
from src.structures.linked_list import LinkedList


class Stack:
    def __init__(self):
        self.list = LinkedList()
        self.min_arr = []

    def pop(self):
        """Берёт элемент сверху стэка"""
        if self.list.is_empty():
            raise StackIsEmptyException()

        value = self.list.pop_front()

        if self.min_arr and value == self.min_arr[-1]:
            self.min_arr.pop()

        return value

    def push(self, x: int) -> None:
        """Добавляет на вверх стэка"""

        self.list.prepend(x)
        if not self.min_arr or x <= self.min_arr[-1]:
            self.min_arr.append(x)

    def is_empty(self) -> bool:
        """Проверяет пустой ли стэк пустым """

        return self.list.is_empty()

    def min(self) -> int:
        """Минимум стэка"""

        if not self.min_arr:
            raise StackIsEmptyException()
        return self.min_arr[-1]

    def peek(self) -> int:
        """Смотрим на вершину стека, не снимая элемент"""

        if self.list.is_empty():
            raise StackIsEmptyException()
        return self.list.head.value

    def __len__(self) -> int:
        """Показывает сколько элементов в стэке"""

        return len(self.list)
