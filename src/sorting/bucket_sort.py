from src.sorting.quick_sort import quick_sort


def bucket_sort(a: list[float], buckets: int | None = None) -> list[float]:
    """
    Сортировка по корзинам O(n + k) в среднем.

    :param a: список элементов вещественного типа
    :param buckets: количество корзин (если None — берём len(a))
    :return: новый отсортированный список
    """

    if not a:
        return []

    n = len(a)

    # Если пользователь не указал количество корзин — используем длину массива
    num_buckets = buckets if buckets is not None else n

    minimum = min(a)
    maximum = max(a)

    # Если все элементы равны — просто вернуть копию
    if minimum == maximum:
        return a

    # создаём корзины
    bucket_list = [[] for _ in range(num_buckets)]

    # распределяем элементы по корзинам
    for value in a:
        index = int((value - minimum) / (maximum - minimum) * (num_buckets - 1))
        bucket_list[index].append(value)

    # сортируем каждую корзину
    for i in range(num_buckets):
        bucket_list[i] = quick_sort(bucket_list[i])

    # объединяем результат
    result = []
    for bucket in bucket_list:
        result.extend(bucket)

    return result
