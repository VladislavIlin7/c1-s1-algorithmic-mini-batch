import random


def nearly_sorted(n: int, swaps: int, *, seed=None) -> list[int]:
    """
    Возвращает почти отсортированный список из чисел от 0 до n с заданным числом перестановок

    :param n: размер списка
    :param swaps: количество случайных перестановок элементов
    :param seed: фиксированное значение генератора случайных чисел
    :return: почти отсортированный список чисел
    """

    if n <= 0:
        return []

    if seed is not None:
        random.seed(seed)

    arr = list(range(n))

    for _ in range(swaps):
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        arr[i], arr[j] = arr[j], arr[i]

    return arr
