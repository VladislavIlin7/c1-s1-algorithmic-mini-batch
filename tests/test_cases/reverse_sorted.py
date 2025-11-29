def reverse_sorted(n: int) -> list[int]:
    """
    Возвращает список из n чисел отсортированных в обратном порядке

    :param n: количество элементов
    :return: список чисел от n-1 до 0
    """

    if n <= 0:
        return []
    return list(range(n - 1, -1, -1))
