from src.benchmarks.timeit_once import timeit_once


def benchmark_sorts(arrays: dict[str, list], algos: dict[str, callable]) -> dict[str, dict[str, float]]:
    """
    Запускает все сортировки из algos на всех массивах из arrays и измеряет время работы каждой

    :param arrays: словарь с наборами данных, где ключ это имя теста, а значение список чисел
    :param algos: словарь алгоритмов сортировки, где ключ это название, а значение функция
    :return: словарь с временем выполнения каждой сортировки на каждом наборе данных
    """
    results = {}

    for arr_name, arr in arrays.items():
        results[arr_name] = {}

        for algos_name, algo in algos.items():
            arr_copy = arr.copy()
            t = timeit_once(algo, arr_copy)
            results[arr_name][algos_name] = t

    return results
