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
        buckets = [[] for _ in range(10)]

        for num in a:
            index = (num // exp) % 10
            buckets[index].append(num)

        a = [num for bucket in buckets for num in bucket]

        exp *= 10

    return a
