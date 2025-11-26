from src.structures.node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0



    def append(self, value: int) -> None:
        """Добавляет элемент в конец связанного списка"""

        new_node = Node(value)

        if self.size == 0:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def prepend(self, value) -> None:
        """Добавить элемент в начало связанного списка"""

        new_node = Node(value, next=self.head)
        self.head = new_node
        if self.size == 0:
            self.tail = new_node
        self.size += 1

    def pop_front(self) -> int:
        """Удаляет значение из начала связанного списка"""

        if self.size == 0:
            raise IndexError("pop from empty linked list")
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        if self.size == 0:
            self.tail = None
        return value

    def is_empty(self) -> bool:
        """Проверяет пустой ли связанный список пустым """

        return self.size == 0

    def __len__(self) -> int:
        """Показывает сколько элементов в связанном списке"""

        return self.size
