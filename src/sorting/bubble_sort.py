def bubble_sort(a: list[int]) -> list[int]:
    """Простой алгоритм. Проходим по списку и меняем соседей, если они стоят неправильно"""

    n = len(a)
    for i in range(len(a)):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a