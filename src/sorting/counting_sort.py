def counting_sort(a: list[int]) -> list[int]:
    """
    Подсчитываем сколько раз встречается каждое число и по этим данным собираем отсортированный список

    :param a: список целых чисел значения которых не должны сильно отличаться друг от друга
    :return: новый отсортированный список
    """

    if not a:
        return []

    minimum = min(a)
    maximum = max(a)
    k = maximum - minimum + 1
    count = [0] * k

    # частоты
    for x in a:
        count[x - minimum] += 1

    # префиксные суммы -> позиции (стабильность)
    for i in range(1, k):
        count[i] += count[i - 1]

    # строим результат справа-налево (стабильно)
    res = [0] * len(a)
    for x in reversed(a):
        idx = x - minimum
        count[idx] -= 1
        res[count[idx]] = x
    return res
