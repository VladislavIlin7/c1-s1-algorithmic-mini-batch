import sys

from src.cli.algorithms_menu import algorithms_menu
from src.cli.sort_menu import sort_menu
from src.cli.stack_menu import stack_menu


def main() -> None:
    """
    Главное меню CLI
    """

    while sys.stdin:
        print("\n=== Главное меню ===")
        print("1 - Сортировки")
        print("2 - Стек")
        print("3 - Алгоритмы (факториал, Фибоначчи)")
        print("0 - Выход")

        choice = input("> ").strip()

        if choice == "1":
            sort_menu()
        elif choice == "2":
            stack_menu()
        elif choice == "3":
            algorithms_menu()
        elif choice == "0":
            print("Выход из программы")
            break
        else:
            print("Неизвестная команда попробуйте ещё раз")


if __name__ == "__main__":
    main()
