def radix_sort(a: list[int]) -> list[int]:
    """
    Поразрядная сортировка для списка неотрицательных целых чисел

    :param a: список натуральных и неотрицательных целых чисел
    :return: новый отсортированный список
    """

    if not a:
        return []

    max_num = max(a)
    exp = 1

    while max_num // exp > 0:
        n = len(a)
        output = [0] * n
        count = [0] * 10

        # Подсчивает количество вхождений каждой цифры
        for num in a:
            index = (num // exp) % 10
            count[index] += 1

        # Преобразовать count[] в фактические позиции
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Построить выходной массив (в обратном порядке для стабильности)
        for i in range(n - 1, -1, -1):
            index = (a[i] // exp) % 10
            output[count[index] - 1] = a[i]
            count[index] -= 1

        # Копировать вывод в arr[]
        for i in range(n):
            a[i] = output[i]

        exp *= 10

    return a
