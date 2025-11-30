from src.cli.generate_base_array import generate_base_array
from src.cli.parse_manual_input import parse_manual_input
from tests.test_cases.rand_float_array import rand_float_array
from tests.test_cases.rand_int_array import rand_int_array



def choose_array(algo_name: str) -> list[int] | list[float] | None:
    """
    Диалог выбора массива для сортировки с учетом ограничений алгоритма.
    Не вываливается в меню сортировок при ошибке ввода, а просит ввести ещё раз.
    """
    while True:
        print("\nКак получить массив")
        print("1 - Ввести вручную")
        print("2 - Сгенерировать случайный")
        print("3 - Почти отсортированный")
        print("4 - С большим количеством повторов")
        print("5 - Обратный порядок")
        print("0 - Отмена")

        choice = input("> ").strip()

        if choice == "0":
            # явная отмена → выходим в меню сортировок
            return None

        # ----- РУЧНОЙ ВВОД -----
        if choice == "1":
            while True:
                line = input(
                    "Введите числа через пробел "
                    "(или пустую строку/`back` чтобы вернуться к выбору способа): "
                ).strip()

                if line == "" or line.lower() == "back":
                    # вернуться к выбору способа получения массива
                    break

                arr = parse_manual_input(algo_name, line)
                if arr is not None:
                    return arr

            # вернулись из внутреннего цикла — снова показать меню способов
            continue

        # дальше — генерация массивов
        if choice not in {"2", "3", "4", "5"}:
            print("Неизвестный вариант, попробуйте ещё раз")
            continue

        # спрашиваем размер массива до тех пор, пока не будет корректный
        while True:
            try:
                n = int(input("Размер массива n: "))
            except ValueError:
                print("Нужно ввести целое число")
                continue

            if n <= 0:
                print("Размер должен быть > 0")
                continue

            break  # корректный n

        # базовый массив целых
        base = generate_base_array(choice, n)
        if base is None:
            continue

        if algo_name == "bucket":
            if choice == "2":
                # для случайных значений лучше сразу вещественные
                return rand_float_array(n, lo=-10000.0, hi=10000.0)
            # для остальных вариантов просто переводим int -> float
            return [float(x) for x in base]

        if algo_name == "radix":
            if choice == "2":
                # отдельная генерация: сразу неотрицательные
                return rand_int_array(n, 0, 10000)
            if any(x < 0 for x in base):
                print("Для radix сортировки нужны неотрицательные целые числа")
                # остаёмся в choose_array, а не вываливаемся в меню сортировок
                continue
            return base

        # остальные сортировки работают с целыми
        return base