from src.benchmarks.benchmark_sorts import benchmark_sorts
from src.constants import ALL_SORTS
from src.sorting.quick_sort import quick_sort
from tests.test_cases.rand_int_array import rand_int_array
from tests.test_cases.nearly_sorted import nearly_sorted
from tests.test_cases.many_duplicates import many_duplicates
from tests.test_cases.reverse_sorted import reverse_sorted


def run_benchmarks(repeats: int = 10) -> None:
    """
    Запускает бенчмарки для всех сортировок несколько раз и печатает среднее время работы

    :param repeats: сколько раз повторять измерение для усреднения
    :return: функция ничего не возвращает, печатает результат в консоль
    """

    sizes = [100, 1000, 5000]
    arrays: dict[str, list[int]] = {}

    for n in sizes:
        arrays[f"random_{n}"] = rand_int_array(n, 0, 10000, seed=1)
        arrays[f"nearly_{n}"] = nearly_sorted(n, swaps=n // 10, seed=1)
        arrays[f"duplicates_{n}"] = many_duplicates(n, seed=1)
        arrays[f"reverse_{n}"] = reverse_sorted(n)

    # создаём словарь для суммирования времени
    sum_results: dict[str, dict[str, float]] = {}

    for _ in range(repeats):
        run_result = benchmark_sorts(arrays, ALL_SORTS)

        # суммируем результаты
        for arr_name, row in run_result.items():
            if arr_name not in sum_results:
                sum_results[arr_name] = {}

            for algo_name, t in row.items():
                sum_results[arr_name][algo_name] = (
                        sum_results[arr_name].get(algo_name, 0.0) + t
                )

    # усредняем
    avg_results = {
        arr_name: {algo: t / repeats for algo, t in row.items()}
        for arr_name, row in sum_results.items()
    }

    for arr_name, row in avg_results.items():
        print(f"\n=== {arr_name} ===")

        items = list(row.items())
        sorted_items = quick_sort(items, key=lambda x: x[1])

        for algo_name, t in sorted_items:
            print(f"{algo_name:10s}:{t:.6f} сек")
