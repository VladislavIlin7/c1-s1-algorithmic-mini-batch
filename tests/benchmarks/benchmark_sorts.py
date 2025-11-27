from tests.benchmarks.timeit_once import timeit_once


def benchmark_sorts(arrays: dict[str, list], algos: dict[str, callable]) -> dict[str, dict[str, float]]:
    """
    Запускает каждую сортировку из algos на каждом массиве из arrays
    и возвращает словарь с временами работы
    """
    results = {}

    for arr_name, arr in arrays.items():
        results[arr_name] = {}

        for algos_name, algo in algos.items():
            arr_copy = arr.copy()
            t = timeit_once(algo, arr_copy)
            results[arr_name][algos_name] = t

    return results
