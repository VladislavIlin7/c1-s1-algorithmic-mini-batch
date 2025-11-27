from src.algorithms.factorial import factorial
from src.algorithms.factorial_recursive import factorial_recursive
from src.algorithms.fibo import fibo
from src.algorithms.fibo_recursive import fibo_recursive
from src.power import power_function


def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """



    print(factorial(10))
    print(factorial_recursive(10))
    print(fibo(10))
    print(fibo_recursive(10))


if __name__ == "__main__":
    main()
